import scrapy


class SopcastSpider(scrapy.Spider):
    name = "sopspy"

    def start_requests(self):
        urls = [
            'http://livetv.sx/team/1_363_446_manchester_city/broadcasts/'
        ]

        for link in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'sops-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
