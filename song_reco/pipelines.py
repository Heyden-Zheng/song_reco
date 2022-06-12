# useful for handling different item types with a single interface
import pymysql
import scrapy
import time
from scrapy.pipelines.files import FilesPipeline


class SongRecoPipeline:
    # 定义用于输出数据到MySQL数据库的Pipeline类
    def process_item(self, item, spider):
        # 通过pymysql对本地数据库进行连接，并且指定要连接的数据库名、用户名和密码
        db = pymysql.connect(host="Localhost", user="haodong", password="123456", db="song_reco", charset="utf8")
        cursor = db.cursor()  # 获取db的游标对象，用于对事物进行处理

        # 根据提取的数据进行再次处理加工，转换成最终存储到数据库中的类型，item[""]是个list

        ranking = item["ranking"]  # 排名
        song_name = item["song_name"]  # 歌名
        time = item["time"]  # 时长
        singer = item["singer"]  # 歌手
        style = item["style"]  # 风格

        # 对数据库进行插入操作，将提取到的item对象中的数据插入到song_reco数据库的song_infos数据表中
        cursor.execute(
            'INSERT INTO song_infos(ranking,song_name,time,singer,style) VALUES (%s,%s,%s,%s,%s)',
            (ranking, song_name, time, singer, style)
        )

        # 提交事务
        db.commit()
        # 关闭游标对象cursor，以及数据库对象db
        cursor.close()
        return item  # 将item返回给下一个将被执行的管道类


class MusicDownloadPipeline(FilesPipeline):

    # 根据链接请求下载
    def get_media_requests(self, item, info):
        song_url = item['song_url']
        print("SongUrl:", song_url)
        try:
            yield scrapy.Request(song_url, meta=item)
            time.sleep(10)
        except:
            print('Pipeline：歌曲下载失败...')

    # 自定义文件下载地址和文件名
    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta['item']
        # file_path = item['singer']  # 根据歌手名分类存放歌曲
        # file_name = '{}-{}'.format(item['song_name'], item['singer']+'.mp3')  # 歌曲文件名
        file_name = item['song_name'] + item['singer'] + '.mp3'
        # return '%s%s' % (file_path, file_name)
        return file_name

    def item_completed(self, results, item, info):
        # 将文件的下载路径取出来（文件夹名/文件名）
        # song_path = results[0][1]
        # item['song_path'] = song_path
        print('Result:', item['song_url'])
        return item
