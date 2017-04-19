import scrapy
from scrapy_splash import SplashRequest

class ratSpider(scrapy.Spider):
	name = "rat2"
	start_urls = [
            'http://localhost:8050/render.html?url=https://www.thertastore.com/kitchen-cabinets/rta-kitchen-cabinets/brilliant-white-shaker.html&timeout=3-&wait=5'
	]

	def start_request(self):
		for url in self.start_urls:
			yield scrapy.Request(url, self.parse_style)

#	def parse(self, response):
		#for item in response.css('li.item'):
		#	new_url = item.css("h2.product-name").css('a::attr(href)').extract_first()
		#j	yield SplashRequest(new_url, self.parse_style, endpoint='render.html', args= {'wait':0.5})

	def parse_style(self, response):
		for item_container in response.css('div.item-info-container'):
			yield{
				'name':item_container.css('div.items-name').css('span::text').extract_first()
			}
