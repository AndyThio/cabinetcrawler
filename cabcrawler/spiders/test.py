import scrapy
from scrapy_splash import SplashRequest

class ratSpider(scrapy.Spider):
	name = "test"

	def start_request(self):
		start_urls = [
			'www.example.com'
		]
		for url in start_urls:
			yield SplashRequest(url, self.parse, args={'wait': 0.5})
	def parse(self, response):
		filename = 'test.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)
