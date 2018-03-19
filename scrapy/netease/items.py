# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    username = scrapy.Field()
    post_time = scrapy.Field()
    replies = scrapy.Field()
    views = scrapy.Field()

class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    thread_id = scrapy.Field()
    username = scrapy.Field()
    userid = scrapy.Field()
    post_level = scrapy.Field()
    poston = scrapy.Field()
    appsign = scrapy.Field()