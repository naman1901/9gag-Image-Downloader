from urllib.request import urlopen
from linkFinder import LinkFinder
from functions import *

class Spider:

	# Class variables shared among all instances
	projectName = ''
	baseURL = ''
	domainName = ''
	queueFile = ''
	crawledFile = ''
	queue = set()
	crawled = set()


	def __init__(self, projectName, baseURL, domainName):
		Spider.projectName = projectName
		Spider.baseURL = baseURL
		Spider.domainName = domainName
		Spider.queueFile = Spider.projectName + '/queue.txt'
		Spider.crawledFile = Spider.projectName + '/crawled.txt'
		self.boot()
		self.crawlPage('First Spider', Spider.baseURL)

	@staticmethod
	def boot():
		createProjectDir(Spider.projectName)
		createDataFiles(Spider.projectName, Spider.baseURL)
		Spider.queue = fileToSet(Spider.queueFile)
		Spider.crawled = fileToSet(Spider.crawledFile)

	@staticmethod
	def crawlPage(threadName, pageURL):
		if pageURL not in Spider.crawled:
			print(threadName + ' at page ' + pageURL)
			print('Pages in Queue: ' + str(len(Spider.queue)) + " | Crawled Pages: " + str(len(Spider.crawled)))
			Spider.addLinksToQueue(Spider.gatherLinks(pageURL))
			if pageURL in Spider.queue:
				Spider.queue.remove(pageURL)
			Spider.crawled.add(pageURL)
			Spider.updateFiles()

	@staticmethod
	def gatherLinks(pageURL):
		htmlString = ''
		try:
			response = urlopen(pageURL)
			if 'text/html' in response.getheader('Content-Type'):
				htmlBytes = response.read()
				htmlString = htmlBytes.decode("utf-8")
			finder = LinkFinder(Spider.baseURL, pageURL)
			finder.feed(htmlString)
		except:
			print("Error: Cannot crawl the page at " + pageURL)
			return set()
		return finder.returnLinks()

	@staticmethod
	def addLinksToQueue(links):
		for link in links:
			if Spider.domainName not in link:
				continue
			if link not in Spider.crawled:
				Spider.queue.add(link)

	@staticmethod
	def updateFiles():
		setToFile(Spider.queue, Spider.queueFile)
		setToFile(Spider.crawled, Spider.crawledFile)