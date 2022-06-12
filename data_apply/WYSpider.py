import scrapy
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Song_Reco.items import SongRecoItem


class WYSpider(scrapy.Spider):
    name = 'wy_spider'  # 爬虫名，通过它执行程序
    allowed_domains = ['music.163.com']
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'

    # 初始化Song_Reco时，创建driver
    def __init__(self):
        super(WYSpider, self).__init__(name='wy_spider')
        # 实例化一个启动参数对象
        options = webdriver.ChromeOptions()
        # 添加启动参数（设置浏览器大小）
        options.add_argument('--window-size=960,600')
        # 设置无头浏览器（测试时建议关闭）
        # options.add_argument('--headless')
        # 将参数对象传入Chrome，则启动了一个自定义的Chrome
        self.driver = webdriver.Chrome(chrome_options=options)

    # 爬取网站第一页的数据
    def start_requests(self):
        # 起始url
        start_url = 'https://music.163.com/discover/toplist?id=3778678'
        yield scrapy.Request(start_url, self.parse, dont_filter=True)

    def parse(self, response):
        # 生成一个字典类型的item对象，存储用于推荐的歌曲信息
        item = SongRecoItem()

        # 先找到iframe的名称
        iframe_name = response.xpath('/html/body/iframe/@name').extract()[0]

        # 根据iframe的名称，进入iframe
        self.driver.switch_to.frame("contentFrame")  # contentFrame是iframe的名字
        # 获取iframe中的歌曲列表
        song_list = self.driver.find_elements(by=By.XPATH,
                                              value='/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/table/tbody/tr')

        # 依次寻找热歌榜单曲
        i = 1
        # 创建风格列表
        style_list = ['流行', '摇滚', '民谣', '电子', '说唱', '轻音乐', '爵士', 'R&B', '古风']

        for song in song_list:
            print('第' + str(i) + '次')
            # 排名
            ranking = song.find_element(by=By.XPATH,
                                        value='../tr[' + str(i) + ']/td[1]/div/span').text
            # 歌曲名
            song_name = song.find_element(by=By.XPATH,
                                          value='../tr[' + str(i) + ']/td[2]/div/div/div/span/a/b').get_attribute(
                'title')
            # 时长
            song_time = song.find_element(by=By.XPATH,
                                          value='../tr[' + str(i) + ']/td[3]/span').text
            # 歌手
            singer = song.find_element(by=By.XPATH,
                                       value='../tr[' + str(i) + ']/td[4]/div').get_attribute('title')
            # 风格
            style = random.choice(style_list)

            # 歌曲url
            raw_song_url = song.find_element(by=By.XPATH,
                                             value='../tr[' + str(i) + ']/td[2]/div/div/div/span/a').get_attribute(
                'href')
            # 用正则表达式截取url，只取id的数字部分；或者用字符串方法截取S
            song_id = raw_song_url[30:]
            # 构造歌曲下载链接
            song_url = 'http://music.163.com/song/media/outer/url?id=' + song_id + '.mp3'

            print('歌曲信息:', ranking, song_name, song_time, singer, style, song_url)

            item["ranking"] = ranking  # 排名
            item["song_name"] = song_name  # 歌曲名
            item["time"] = song_time  # 时长
            item["singer"] = singer  # 歌手
            item["style"] = style  # 风格
            item["song_url"] = song_url
            yield item  # 将歌曲信息存储到数据库
            # self.driver.back()
            time.sleep(1)
            i += 1
        self.driver.close()
