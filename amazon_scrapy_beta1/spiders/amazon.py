import scrapy
from scrapy import Request
from amazon_scrapy_beta1.items import ProductItem
import re
import logging


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    q = "Dyson"
    base_url = "https://www.amazon.com"
    start_urls = [f"https://www.amazon.com/s?k={q}"]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Host": "www.amazon.com",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1"
    }

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'RETRY_TIMES': 5,
        'RETRY_HTTP_CODES': [500, 502, 503, 504, 522, 524, 408, 429, 403],
        'COOKIES_ENABLED': True,
        'LOG_LEVEL': 'INFO'
    }

    def start_requests(self):
        yield Request(
            url=self.start_urls[0],
            headers=self.headers,
            callback=self.parse,
            meta={"page": 1, "keyword": self.q},
            dont_filter=True
        )

    def parse(self, response):
        if "captcha" in response.text.lower():
            self.logger.warning("Detected CAPTCHA page, retrying with different User-Agent")
            yield Request(
                url=response.url,
                headers=self.headers,
                callback=self.parse,
                dont_filter=True
            )
            return

        # Save response for debugging
        with open('amazon_response.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        products = response.css("div.s-result-item[data-component-type=s-search-result]")
        self.logger.info(f"Found {len(products)} products on page")
        
        for product in products:
            try:
                item = ProductItem()
                
                # Extract product URL
                relative_url = None
                url_selectors = [
                    "h2 a::attr(href)",
                    "a.a-link-normal.s-no-outline::attr(href)",
                    "div.rush-component a.a-link-normal::attr(href)",
                    ".a-link-normal.s-underline-text::attr(href)"
                ]
                
                for selector in url_selectors:
                    relative_url = product.css(selector).get()
                    if relative_url:
                        break
                
                if not relative_url:
                    self.logger.warning("No URL found for product, skipping")
                    continue
                    
                product_detail_url = self.base_url + relative_url if not relative_url.startswith("http") else relative_url
                
                # Extract product name
                name = None
                name_selectors = [
                    "h2 a span::text",
                    "h2 span.a-text-normal::text",
                    "span.a-size-medium::text",
                    ".a-text-normal::text",
                    "h2 a::text"
                ]
                
                for selector in name_selectors:
                    name = product.css(selector).get()
                    if name:
                        name = name.strip()
                        if name:
                            break
                
                if not name:
                    # Try XPath as fallback
                    name = product.xpath('.//h2//text()').get()
                    if name:
                        name = name.strip()
                
                if not name:
                    self.logger.warning("No name found for product, skipping")
                    continue
                    
                name = re.sub(r"['\"\\n]", "", name)
                
                # Extract ASIN
                asin = product.css("::attr(data-asin)").get() or ""
                
                # Extract ratings
                n_ratings = None
                rating_selectors = [
                    'span[aria-label*="stars"] span::text',
                    'div.a-row.a-size-small span:contains("stars")::text',
                    '.a-icon-alt::text'
                ]
                
                for selector in rating_selectors:
                    n_ratings = product.css(selector).get()
                    if n_ratings:
                        break
                
                n_ratings = n_ratings or "0"
                
                # Extract price
                price_text = None
                price_selectors = [
                    "span.a-offscreen::text",
                    "span.a-price-whole::text",
                    ".a-price .a-offscreen::text"
                ]
                
                for selector in price_selectors:
                    price_text = product.css(selector).get()
                    if price_text:
                        break
                
                price = re.sub(r"[\$,]", "", price_text or "0")
                
                # Extract number of ratings
                no_of_ratings = None
                rating_count_selectors = [
                    "span.a-size-base.s-underline-text::text",
                    ".a-link-normal .a-size-base::text",
                    "a[href*='customerReviews'] .a-size-base::text"
                ]
                
                for selector in rating_count_selectors:
                    no_of_ratings = product.css(selector).get()
                    if no_of_ratings:
                        break
                
                no_of_ratings = no_of_ratings or "0"
                
                # Extract offers/deals
                offers = None
                offer_selectors = [
                    ".a-badge-text::text",
                    ".a-badge-label::text",
                    "span[data-a-badge-color='deal']::text"
                ]
                
                for selector in offer_selectors:
                    offers = product.css(selector).get()
                    if offers:
                        break
                
                offers = offers or ""

                item.update({
                    "asin": asin,
                    "name": name,
                    "price": float(price),
                    "no_of_ratings": no_of_ratings,
                    "n_ratings": n_ratings,
                    "offers": offers,
                    "product_detail_url": product_detail_url
                })
                
                yield item

            except Exception as e:
                self.logger.error(f"Error processing product: {str(e)}")
                continue

        # Check for next page
        next_page = response.css("a.s-pagination-next::attr(href)").get()
        if next_page:
            next_url = self.base_url + next_page if not next_page.startswith("http") else next_page
            page = response.meta.get("page", 1)
            self.logger.info(f"Moving to page {page + 1}")
            yield Request(
                url=next_url,
                headers=self.headers,
                callback=self.parse,
                meta={"page": page + 1, "keyword": self.q},
                dont_filter=True
            )
