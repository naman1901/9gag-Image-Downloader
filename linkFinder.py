from html.parser import HTMLParser
from urllib import parse
from imageDownloader import ImageDownloader

class LinkFinder(HTMLParser):

	def __init__(self, baseURL, pageURL):
		super().__init__()
		self.baseURL = baseURL
		self.pageURL = pageURL
		self.links = set()

	def error(self, message):
		pass

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.baseURL, value)
					self.links.add(url)
		elif tag == 'img':
			for (attribute, value) in attrs:
				if attribute == "src":
					url = parse.urljoin(self.baseURL, value)
					ImageDownloader.downloadImage(url)
                                        

	def returnLinks(self):
		return self.links

