import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["www.themoviedb.org"]
    start_urls = ["http://www.themoviedb.org/"]

    def parse(self, response):
        pass
