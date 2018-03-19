# -*- coding: utf-8 -*-
# 网易手机游戏官网论坛›荒野行动› 荒野行动|综合讨论
import scrapy
import re
from netease.items import ThreadItem, PostItem


class ForumSpider(scrapy.Spider):
    name = 'forum'
    page_num = 576
    urlform = 'http://hy.16163.com/forum-1905-{}.html'
    start_urls = [urlform.format(page_num)]

    def parse(self, response):
        thread_list_table = response.xpath('//table[@id="threadlisttableid"]/tbody[contains(@id, "normalthread")]')
        for thread in thread_list_table:
            thread_item = ThreadItem()
            # 获取id
            thread_id = re.search('\d+',thread.xpath("./@id").extract_first()).group(0)
            # 获取标题
            thread_title = thread.css('.xst::text').extract_first()
            # 获取链接地址
            thread_url = thread.css('.xst::attr(href)').extract_first()
            url = response.urljoin(thread_url)
            # 获取发帖人
            if thread.css('.author').xpath('./a'):
                username = thread.css('.author').xpath('./a/text()').extract_first()
            else:
                username = "匿名"
            # 获取发帖时间
            post_time = thread.css('.post-time::text').extract_first().strip()
            # 获取回复数和阅读数
            replies = thread.css('.replies::text').extract_first().strip()
            views = thread.css('.views::text').extract_first().strip()

            thread_item["id"] = thread_id
            thread_item["title"] = thread_title
            thread_item["url"] = url
            thread_item["username"] = username
            thread_item["post_time"] = post_time
            thread_item["replies"] = replies
            thread_item["views"] = views

            yield thread_item

            # 抓取话题里面的帖子信息
            yield scrapy.Request(url = url, meta={'thread_id':thread_id},callback=self.parse_thread)

        # 页面数减一，抓取前一页，直到第一页为止
        self.page_num -=1
        if self.page_num>0:
            next_page_url = self.urlform.format(self.page_num)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_thread(self, response):
        thread_id = response.meta["thread_id"]
        postlist = response.xpath('//div[@id="postlist"]/div[contains(@id, "post_")]')
        for post in postlist:
            post_item = PostItem()
            # 获取帖子id
            post_id = re.search('\d+',post.xpath("./@id").extract_first()).group(0)

            content = post.xpath('./table/tr[1]')
            user_content = content.xpath('./td[@class="pls"]')
            post_content = content.xpath('./td[@class="plc"]')
            # 获取用户名和id
            if user_content.xpath('.//div[@class="authi"]'):
                username = user_content.xpath('.//div[@class="authi"]/a/text()').extract_first()
                userid = re.search('\d+', user_content.xpath('.//div[@class="authi"]/a/@href').extract_first()).group(0)
            else:
                username = "匿名"
                userid = 0
            # 获取楼层
            level_content = post_content.xpath('.//div[@class="pi"]/strong')
            post_level = level_content.xpath('string(.)').extract_first().strip()
            # 获取发表日期
            poston_content = post_content.xpath('.//div[@class="authi"]')
            poston = poston_content.xpath('./em/text()').extract_first().replace("发表于", "").strip()
            # 获取app标识：0表示为非app，1表示为app发表
            appsign = 0
            if poston_content.xpath('./span[@class="xg1"]'):
                appsign = 1

            post_item["id"] = post_id
            post_item["thread_id"] = thread_id
            post_item["username"] = username
            post_item["userid"] = userid
            post_item["post_level"] = post_level
            post_item["poston"] = poston
            post_item["appsign"] = appsign

            yield post_item

        # 下一页地址
        if response.css('.nxt'):
            next = response.css('.nxt::attr("href")').extract_first()
            next_url = response.urljoin(next)
            yield scrapy.Request(url = next_url, meta={'thread_id':thread_id},callback=self.parse_thread)
