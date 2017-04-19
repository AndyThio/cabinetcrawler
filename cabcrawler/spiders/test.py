import scrapy
from scrapy_splash import SplashRequest

class ratSpider(scrapy.Spider):
    name = "hope"
    start_urls = [
        'https://www.thertastore.com/kitchen-cabinets/rta-kitchen-cabinets/brilliant-white-shaker.html'
    ]

    def start_request(self):
        lua_script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(10))
            return{
                html = splash:html(),
            }
        end
        """
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,args={'lua_source':lua_script,}, endpoint='execute')


    def parse(self, response):
        #filename = 'resultshtml.html'
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        for item_container in response.css('div.item-info-container'):
            yield{
                    'name' : item_container.css('div.items-name').css('span::text').extract_first(),
            }
