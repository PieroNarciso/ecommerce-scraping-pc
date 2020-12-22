import scrapy
from scrapy.http.response.html import HtmlResponse as Response
from scrapy.selector.unified import Selector

from ..types import Selectors

from datetime import datetime


class MixinEcommerceSpider(object):
    selectors: Selectors
    
    def parse(self, response: Response):
        for product in response.css(f"{self.selectors['product']}"):
            yield {
                "title": self.parse_title(product),
                "img": self.parse_image(product),
                "price": self.parse_price(product),
                "detail": self.parse_detail(product)
            }
        next_page = response.css(f"{self.selectors['next_page']}").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_title(self, product: Selector):
        return product.css(f"{self.selectors['title']}").get()

    def parse_image(self, product: Selector):
        return product.css(f"{self.selectors['image']}").get()

    def parse_price(self, product: Selector):
        return product.css(f"{self.selectors['price']}").get()

    def parse_detail(self, product: Selector):
        return product.css(f"{self.selectors['detail_url']}").get()



class SercoplusSpider(MixinEcommerceSpider, scrapy.Spider):
    name = "sercoplus"
    custom_settings = {
            "FEED_FORMAT": "csv",
            "FEED_URI": "./data/sercoplus-{}.csv".format(datetime.now() \
                    .strftime("%m-%d-%Y"))
        }
    selectors = {
        "product": "div.product-container.product-style",
        "title": "h5.product-name a::attr(title)",
        "image": "img.img-fluid::attr(data-original)",
        "price": "span.price.product-price::text",
        "detail_url": "a.product-cover-link::attr(href)",
        "next_page": "li > a.next::attr(href)" 
    }
    
    def __init__(self, query: str=None, *args, **kwargs):
        url = "https://www.sercoplus.com/busqueda?controller=search&s=%s" % query
        self.start_urls = [
            url
        ]
        scrapy.Spider.__init__(self, *args, **kwargs)


class ImpactoSpider(MixinEcommerceSpider, scrapy.Spider):
    name = "impacto"
    custom_settings = {
            "FEED_FORMAT": "csv",
            "FEED_URI": "./data/impacto-{}.csv".format(datetime.now() \
                    .strftime("%m-%d-%Y"))
        }
    selectors = {
            "product": "div.single-product.mt-1",
            "title": "h4.product-title > a::text",
            "image": "img.first-image::attr(data-src)",
            "price": "span.price-sale::text",
            "detail_url": "div.product-image > a::attr(href)",
            "next_page": "a[rel='next']::attr(href)"
        }

    def __init__(self, query: str=None, *args, **kwargs):
        url = "https://www.impacto.com.pe/catalogo?qsearch=%s" % query
        self.start_urls = [
                url
            ]
        scrapy.Spider.__init__(self, *args, **kwargs)

    def parse_title(self, product: Selector):
        return product.css(f"{self.selectors['title']}").get() \
                    .strip().replace("\r\n", "")

    def parse_price(self, product: Selector):
        return product.css(f"{self.selectors['price']}").get() \
                    .strip().replace("\r\n", "").replace(" ", "")


class CompuvisionSpider(MixinEcommerceSpider, scrapy.Spider):
    name = "compuvision"
    custom_settings = {
            "FEED_FORMAT": "csv",
            "FEED_URI": "./data/compuvision-{}.csv".format(datetime.now() \
                    .strftime("%m-%d-%Y"))
        }
    selectors = {
            "product": "div.item-product",
            "title": "a.product_name::attr(title)",
            "image": "img.first-image::attr(src)",
            "price": "span.price::text",
            "detail_url": "a.product_name::attr(href)",
            "next_page": "a[rel='next']::attr(href)"
        }

    def __init__(self, query: str=None, *args, **kwargs):
        url = "http://compuvisionperu.pe/busqueda?s=%s" % query
        self.start_urls = [
                url
            ]
        scrapy.Spider.__init__(self, *args, **kwargs)


class CyCComputerSpider(MixinEcommerceSpider, scrapy.Spider):
    name = "cyccomputer"
    custom_settings = {
            "FEED_FORMAT": "csv",
            "FEED_URI": "./data/cyccomputer-{}.csv".format(datetime.now() \
                    .strftime("%m-%d-%Y"))
        }
    selectors = {
            "product": "div.product-container.item",
            "title": "h5.product-name > a::attr(title)",
            "image": "img.img-responsive::attr(src)",
            "price": "span.price.product-price::text",
            "detail_url": "h5.product-name > a::attr(href)",
            "next_page": "li.pagination_next > a::attr(href)"
        }

    def __init__(self, query: str=None, *args, **kwargs):
        url = "https://www.cyccomputer.pe/buscar?controller=search&orderby=\
                position&orderway=desc&search_query=%s" % query
        self.start_urls = [
                url
            ]
        scrapy.Spider.__init__(self, *args, **kwargs)
