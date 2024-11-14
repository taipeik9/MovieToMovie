import json
import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["www.imdb.com"]

    def start_requests(self):
        with open("graph.json", "r") as f:
            graph = json.load(f)
            ids = list(graph.keys())
        for id in ids[:5]:
            if id[:1] == "tt":
                url = f"https://www.imdb.com/title/{id}"
            elif id[:1] == "nm":
                url = f"https://www.imdb.com/name/{id}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
