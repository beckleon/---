# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from netease.items import ThreadItem, PostItem

class NeteasePipeline(object):
    def __init__(self, mysql_uri, mysql_db, mysql_user, mysql_pw, mysql_port):
        self.mysql_uri = mysql_uri
        self.mysql_user = mysql_user
        self.mysql_pw = mysql_pw
        self.mysql_db = mysql_db
        self.mysql_port = mysql_port

    # 从settings获取MongoDB的设置
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_uri=crawler.settings.get('MYSQL_URI'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_pw=crawler.settings.get('MYSQL_PW'),
            mysql_db=crawler.settings.get('MYSQL_DATABASE'),
            mysql_port = crawler.settings.get('MYSQL_PORT')
        )

    # 打开数据库连接
    def open_spider(self, spider):
        self.connMy = mysql.connector.connect(host=self.mysql_uri,
                                              user=self.mysql_user,
                                              password=self.mysql_pw,
                                              database=self.mysql_db,
                                              port=self.mysql_port,
                                              charset='utf8')
        self.cur = self.connMy.cursor()

    # 关闭数据库连接
    def close_spider(self, spider):
        self.cur.close()
        self.connMy.close()

    def process_item(self, item, spider):
        if isinstance(item, ThreadItem):
            insertSQL = "insert into threads values('{}','{}','{}','{}','{}','{}','{}')".format(
                item["id"],
                item["title"].replace("'","\\'"),
                item["url"],
                item["username"].replace("'","\\'"),
                item["post_time"],
                item["replies"],
                item["views"]
            )
            self.cur.execute(insertSQL)
            self.connMy.commit()
            return item

        if isinstance(item, PostItem):
            insertSQL = "insert into posts values('{}','{}','{}','{}','{}','{}','{}')".format(
                item["id"],
                item["thread_id"],
                item["username"].replace("'", "\\'"),
                item["userid"],
                item["post_level"],
                item["poston"],
                item["appsign"]
            )
            self.cur.execute(insertSQL)
            self.connMy.commit()
            return item

