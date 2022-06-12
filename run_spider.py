# 代替在命令行执行爬虫程序，并将日志文件保存在项目根目录下
import os

os.system('scrapy crawl wy_spider -s LOG_FILE=Song_Reco.log')
