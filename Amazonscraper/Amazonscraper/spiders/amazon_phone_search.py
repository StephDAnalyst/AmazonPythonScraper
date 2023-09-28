import json
import scrapy
from urllib.parse import urljoin
import re
from Amazonscraper.items import AmazonItem

class AmazonSearchProductSpider(scrapy.Spider):
    
    name = "amazon_phone_search"
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=phone&crid=27UWARD05Q18G&sprefix=phone%2Caps%2C385&ref=nb_sb_noss_1']
    

    def discover_product_urls(self, response):
        ## Discover Product URLs
        search_products = response.css("div.s-result-item[data-component-type=s-search-result]")
        for product in search_products:
            relative_url = product.css("h2>a::attr(href)").get()
            product_url = urljoin('https://www.amazon.com/', relative_url).split("?")[0]
            yield response.follow(url=product_url, callback=self.parse_product_data) 
       
        next_page = response.xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']/@href").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.discover_product_urls)
        

    def parse_product_data(self, response):
        image_data = json.loads(re.findall(r"colorImages':.*'initial':\s*(\[.+?\])},\n", response.text)[0])
        variant_data = re.findall(r'dimensionValuesDisplayData"\s*:\s* ({.+?}),\n', response.text)
        feature_bullets = [bullet.strip() for bullet in response.css("#feature-bullets li ::text").getall()]
        color_variants = [color_variant.strip() for color_variant in response.xpath("//li[contains(@class, 'swatch')]/@title").getall()]
        price = response.css('.a-price span[aria-hidden="true"] ::text').get("")
        if not price:
            price = response.css('.a-price .a-offscreen ::text').get("")
        item = AmazonItem()
        item['name'] = response.css("#productTitle::text").get("").strip()
        item['color_variants'] = color_variants
        item['price'] = price
        item['stars'] = response.css("i[data-hook=average-star-rating] ::text").get("").strip()
        item['rating_count'] = response.css("div[data-hook=total-review-count] ::text").get("").strip()
        item['feature_bullets'] = feature_bullets
        item['images'] = image_data
        item['variant_data'] = variant_data

        yield item