import scrapy


class SopcastSpider(scrapy.Spider):
    name = "sopspy"
    urls = [
        'http://livetv.sx/allupcomingsports/1/'
    ]

    def parse(self, response):
        for href in response.xpath('//a/@href').extract():
            yield scrapy.Request(url)
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)
