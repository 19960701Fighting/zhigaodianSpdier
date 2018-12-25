# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from twisted.enterprise import adbapi
from pymysql.cursors import DictCursor


class ZhigaodianPipeline(object):

    def __init__(self):
        prams = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "db": "zhigaodian",
            "charset": "utf8",
            "use_unicode": True,
            "cursorclass": DictCursor
        }
        self.db_pool = adbapi.ConnectionPool('pymysql', **prams)

    def process_item(self, item, spider):

        res = self.db_pool.runInteraction(self.insert_item, item)
        res.addErrback(self.error_item)

        return item

    def insert_item(self, cursor, item):
        item.save(cursor)

    def error_item(self, fail):
        print(fail)

class SaveImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'item':item}) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):

        item = request.meta.get('item')
        img_src = item.get('img_src')[0]
        img_name = img_src.split('/')[-1]
        # 图片保存路径
        img_path = 'brand/' + img_name

        item['image_path'] = 'images/'+ img_path

        return img_path







