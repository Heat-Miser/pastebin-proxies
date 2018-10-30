# -*- coding: utf-8 -*-

# Scrapy settings for pastebin_proxies project
# # For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
# #     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pastebin_proxies'

SPIDER_MODULES = ['pastebin_proxies.spiders']
NEWSPIDER_MODULE = 'pastebin_proxies.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# SER_AGENT = 'pastebin_proxies (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# ONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html# ownload-delay
# See also autothrottle settings and docs
# OWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# ONCURRENT_REQUESTS_PER_DOMAIN = 16
# ONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# OOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# ELNETCONSOLE_ENABLED = False

# Override the default request headers:
# EFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# PIDER_MIDDLEWARES = {
#    'pastebin_proxies.middlewares.PastebinProxiesSpiderMiddleware': 543,
#

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# OWNLOADER_MIDDLEWARES = {
#    'pastebin_proxies.middlewares.PastebinProxiesDownloaderMiddleware': 543,
#

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# XTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# TEM_PIPELINES = {
#    'pastebin_proxies.pipelines.PastebinProxiesPipeline': 300,
#

ITEM_PIPELINES = {
    'pastebin_proxies.pipelines.PastebinProxiesPipeline': 100,
    'pastebin_proxies.pipelines.DuplicatesPipeline': 200,
    'pastebin_proxies.pipelines.RemoveSlowProxies': 300,
}

FEED_STORAGES_BASE = {
    '': 'pastebin_proxies.customexport.CustomFileFeedStorage',
    'file': 'pastebin_proxies.customexport.CustomFileFeedStorage',
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# UTOTHROTTLE_ENABLED = True
# The initial download delay
# UTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# UTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# UTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# UTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html# ttpcache-middleware-settings
# TTPCACHE_ENABLED = True
# TTPCACHE_EXPIRATION_SECS = 0
# TTPCACHE_DIR = 'httpcache'
# TTPCACHE_IGNORE_HTTP_CODES = []
# TTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
