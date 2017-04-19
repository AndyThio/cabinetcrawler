import scrapy
from scrapy_splash import SplashRequest

class ratSpider(scrapy.Spider):
	name = "rat"
	start_urls = [
		'https://www.thertastore.com/kitchen-cabinets/rta-kitchen-cabinets.html'
	]

	def parse(self, response):
		for item in response.css('li.item'):
			new_url = item.css("h2.product-name").css('a::attr(href)').extract_first()
			yield SplashRequest(new_url, self.parse_style, endpoint='render.html', args= {'wait':0.5})

	def parse_style(self, response):
		for item_container in response.css('div.item-container'):
			yield{
				'name':item_container.css('div.items-name').css('span::text')
			}
