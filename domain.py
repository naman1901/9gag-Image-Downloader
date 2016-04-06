from urllib.parse import urlparse

# Get subdomain name (something.else.here.example.com)
def getSubDomainName(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

# Get domain name (example.com)
def getDomainName(url):
	try:
		results = getSubDomainName(url).split('.')
		return results[-2] + '.' + results[-1]			#Returns 2nd last and last entries
	except:
		return ''
