import scrapy


class SongRecoItem(scrapy.Item):
    ranking = scrapy.Field()  # 排名
    song_name = scrapy.Field()  # 歌名
    time = scrapy.Field()  # 时长
    singer = scrapy.Field()  # 歌手
    style = scrapy.Field()  # 风格
    song_url = scrapy.Field()  # 下载链接
    song_path = scrapy.Field()  # 歌曲保存路径（pipeline.py文件需要）

    pass
