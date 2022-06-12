BOT_NAME = 'Song_Reco'

SPIDER_MODULES = ['Song_Reco.spiders']
NEWSPIDER_MODULE = 'Song_Reco.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Song_Reco (+http://www.yourdomain.com)'

# Obey robots.txt rules，必要时可改为False
ROBOTSTXT_OBEY = False
# 设置随机下载时延(0.5-1.5)，避免服务器同时收到大量请求
RANDOMIZE_DOWNLOAD_DELAY = True
# 打印日志的级别
LOG_LEVEL = 'WARNING'

CONCURRENT_REQUESTS = 8  # 爬虫可同时处理8个request，增加并发
DOWNLOAD_TIMEOUT = 10  # 设置下载超时，放弃超过这个时间仍然卡住的连接，继续处理下一个
# 允许重定向
# MEDIA_ALLOW_REDIRECTS = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Song_Reco.middlewares.SongRecoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Song_Reco.middlewares.SongRecoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 替换掉默认的下载中间件
DOWNLOADER_MIDDLEWARES = {
    'Song_Reco.middlewares.SeleniumSongRecoDownloaderMiddleware': 543,
}
# Configure item pipelines
ITEM_PIPELINES = {
    'Song_Reco.pipelines.SongRecoPipeline': 300,
    'Song_Reco.pipelines.MusicDownloadPipeline': 1,
}
FILES_STORE = './musics'
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
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
