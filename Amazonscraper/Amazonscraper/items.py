# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class AmazonItem(scrapy.Item):
    name = scrapy.Field()
    color_variants = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    rating_count = scrapy.Field()
    feature_bullets = scrapy.Field()
    images = scrapy.Field()
    variant_data = scrapy.Field()

