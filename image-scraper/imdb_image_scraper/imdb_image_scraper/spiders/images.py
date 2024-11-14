import json
import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["www.imdb.com"]

    def start_requests(self):
        with open("graph.json", "r") as f:
            graph = json.load(f)
            ids = list(graph.keys())
        for id in ids:
            if id[:2] == "tt":
                url = f"https://www.imdb.com/title/{id}/"
            elif id[:2] == "nm":
                url = f"https://www.imdb.com/name/{id}/"
            else:
                continue
            yield scrapy.Request(url=url, callback=self.parse, meta={"id": id})

    def parse(self, response):
        image_link = response.xpath(
            '//div[@class="ipc-poster ipc-poster--baseAlt ipc-poster--media-radius'
            ' ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2"]'
            '/a[@class="ipc-lockup-overlay ipc-focusable"]/@href'
        ).get()
        if image_link:
            yield response.follow(
                url=image_link, callback=self.parse_image, meta=response.request.meta
            )
        else:
            yield {"id": response.request.meta["id"], "url": None}

    def parse_image(self, response):
        data_image_id = response.request.url.split("/")[-2]
        url = response.xpath(f'//img[@data-image-id="{data_image_id}-curr"]/@src').get()

        yield {"id": response.request.meta["id"], "url": url}
