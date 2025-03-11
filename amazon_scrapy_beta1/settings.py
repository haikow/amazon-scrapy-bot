# Scrapy settings for amazon_scrapy_beta1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "amazon_scrapy_beta1"
COOKIES = 'session-id=131-1492828-1087569; i18n-prefs=USD; ubid-main=135-1392100-9641860; skin=noskin; id_pkel=n1; id_pk=eyJuIjoiMSJ9; JSESSIONID=254B30F9A52A21AA11D26DA391392F1C; session-token="+QaIBJvd0jUI/NmeG+5/Qws7e7967Hs3GDvqHRA45WX9ug1OExY19Tj0W384QknMJuHmzWNEQ2U/omg74ifCEEKNCgX3pArc1j2rko89vQe2Ejs0NLA201tuLkDeSgVpnTkxynMqSLx/O42xrpp7V2XYOLaC8fNItC7gzoNGgE4CE/gOTC+r/AkWdvT0dvsv2Ekc6ZUT3gHtXdWGhjXKJcW6CdJogH0PvVlOGDvOC4YoC33vEdiKSzmFCSv4tdzdzLaSAOMpROdXnY2ITTEhJIZOayxZswTQnBKwkWX5JZ1Yc1/FVrmq2dAQXlJpkfTW3RR0pkimIReNCZDSMbh/ZHJiNOC4KvOpiXQNFm3iq6l6bZv3Vf14TQ=="; x-main="CXfe?Xgs0RTEzuClNXTPgV3ujPFlj?WWVBxWfOKu0X9SXnq1Q?aZsBhlP9M@kU@Y"; at-main=Atza|IwEBIPSSjCEEY2f4dtCU02F-RT5cAk73UW5HxZ1XTywCRHZbt6Bk2vBusMAkUBkGg2E9kMbJfbTB40_4GgXOr_L5cUbe0ewIDNJCnU4bbiwnoucSWnnsRlap-T2G-rqrD2SmHFSjUuRlrjrb4je3LDJbmTPDSc8uWo5IZlJPQie1jQRMGxYWOSB8yluAee3M8EDsofiCGtddI_CebP_jusIhvpZKiK_MU-O5aPGs6Jm8wexD5Q; sess-at-main="XPB6rXcY7l43qRnNbgNSHkbKYVInyVPpUMxuS7J6uZw="; sst-main=Sst1|PQEeqSWgG62dLHdIKB-IW5aJCRTsq7mujwKekiL0RUDtpLKmLxeluQqP7hLl_6a_iZrjCIeSiLY1FO_aWmWvjTNFdjxpMziOim_gLDenoRitUO7XBxJv0rdKnqgHaERbFkE0tVVYRXtBhHIFbJ-_FIADmCrNQc4W5ggQqT8bJHhl5ZYxgk41Lz9kI74XDdP3AnlmSgLx_G7XYRzSuO6NT0XEiq1-oVbv0oU-eoCnDkKjaDjoZyweU2l0dW8Kuaozb_UamIvYKPlgRuf29sewzuvzMdidX9kriadkMCcd8J0-mX0; session-id-time=2082787201l; lc-main=en_US; csm-hit=tb:s-V1ZH0QPRKNYC5VPFYN7H|1741590923230&t:1741590923230&adb:adblk_no'

SPIDER_MODULES = ["amazon_scrapy_beta1.spiders"]
NEWSPIDER_MODULE = "amazon_scrapy_beta1.spiders"

ROBOTSTXT_OBEY = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "amazon_scrapy_beta1 (+http://www.yourdomain.com)"
## settings.py

# USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "amazon_scrapy_beta1.middlewares.AmazonScrapyBeta1SpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "amazon_scrapy_beta1.middlewares.AmazonScrapyBeta1DownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "amazon_scrapy_beta1.pipelines.AmazonScrapyBeta1Pipeline": 300,
    # "amazon_scrapy_beta1.pipelines.PostgreSQLPipeline": 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
## settings.py
DOWNLOAD_DELAY = 5
LOG_LEVEL = "INFO"

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    "amazon_scrapy_beta1.middlewares.RetryMiddleware": 550,
    "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
    "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 1,
}


DATABASE_SETTINGS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "ts123456",
    "host": "localhost",
    "port": "5432",
}


# 配置代理服务器地址和端口
HTTP_PROXY = "http://127.0.0.1:8080"

FAKEUSERAGENT_PROVIDERS = [
    "scrapy_fake_useragent.providers.FakeUserAgentProvider",  # This is the first provider we'll try
    "scrapy_fake_useragent.providers.FakerProvider",  # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    "scrapy_fake_useragent.providers.FixedUserAgentProvider",  # Fall back to USER_AGENT value
]


# jdbc:postgresql://localhost:5432/postgres
