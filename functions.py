import os

#Create separate folders for each website crawled
def createProjectDir(directory):
	if not os.path.exists(directory):
		print('Creating directory %s' %(directory))
		os.makedirs(directory)


#Create a queue for uncrawled pages and a list of crawled pages
def createDataFiles(projectName, baseURL):
	queue = projectName + '/queue.txt'
	crawled = projectName + '/crawled.txt'
	if not os.path.isfile(queue):
		createFile(queue, baseURL + '\n')
	if not os.path.isfile(crawled):
		createFile(crawled, '')


# Function to write data to file
def createFile(fileName, data):
	file = open(fileName, 'w')
	file.write(data)
	file.close()


# Append data to file
def writeToFile(fileName, data):
	with open(fileName, 'a') as file:
		file.write(data + '\n')

# Truncate a file
def truncateFile(fileName):
	with open(fileName, 'w') as file:
		pass


# Convert data from a file to a separate
def fileToSet(fileName):
	results = set()
	with open(fileName, 'rt') as file:
		for line in file:
			results.add(line.replace('\n', ''))
	return results

# Write a set to a file
def setToFile(data, fileName):
	truncateFile(fileName)
	for url in sorted(data):
		writeToFile(fileName, url)
