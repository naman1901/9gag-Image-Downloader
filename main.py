import threading
from queue import Queue
from spider import Spider
from domain import *
from functions import *

PROJECT_NAME = '9gag'
BASE_URL = 'http://9gag.com'
DOMAIN_NAME = getDomainName(BASE_URL)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4

threadQueue = Queue()

Spider(PROJECT_NAME, BASE_URL, DOMAIN_NAME)

def crawl():
	while True:
		queuedLinks = fileToSet(QUEUE_FILE)
		if len(queuedLinks) > 0:
			createJobs()
		else:
			break

# Each link in queued links is a new job
def createJobs():
	for link in fileToSet(QUEUE_FILE):
		threadQueue.put(link)
	threadQueue.join()

# Create worker threads 
def createThreads():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()

def work():
	while True:
		url = threadQueue.get()
		Spider.crawlPage(threading.current_thread().name, url)
		threadQueue.task_done()

createThreads()
crawl()