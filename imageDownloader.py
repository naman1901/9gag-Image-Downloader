from urllib import request
from queue import Queue
import threading
import os

class ImageDownloader:

	imageNumber = 1
	downloadQueue = Queue()
	downloadedImages = set()

	@staticmethod
	def downloadImage(url):
		if url in ImageDownloader.downloadedImages:
			return
		ImageDownloader.createProjectDir()
		ImageDownloader.downloadedImages.add(url)
		ImageDownloader.downloadQueue.put(url)
		t = threading.Thread(target=ImageDownloader.download)
		t.daemon = True
		t.start()

	@staticmethod
	def createProjectDir():
		if not os.path.exists('Images'):
			os.makedirs('Images')

	@staticmethod
	def download():
		dest = "Images/" + str(ImageDownloader.imageNumber) + ".jpg"
		ImageDownloader.imageNumber = ImageDownloader.imageNumber+1
		url = ImageDownloader.downloadQueue.get()
		request.urlretrieve(url, dest)
