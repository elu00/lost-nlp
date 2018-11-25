# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FfscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PostItem(scrapy.Item):
    collection = 'post'
    #unique_fields = ['thread_id','post_no']

    #thread_id = scrapy.Field()
    #user_id = scrapy.Field()
    timestamp = scrapy.Field()
    message = scrapy.Field()
    #quotes = scrapy.Field()
    #post_no = scrapy.Field()
    # post_no is shown on upper right of each post container.

    # post_id is '202020' in the last part of URL: http://metaldetectingforum.com/showpost.php?p=202020
    # But I'm not using post_id right now.