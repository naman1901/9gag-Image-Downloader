
#url = ImageDownloader.downloadQueue.get()
url = str(input('Enter URL'))
dest = url.split('/')
dest = dest[-1]
print(dest)




