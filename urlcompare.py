import os

#throw target url into urlcompare, the function would check if the url is in blacklists
#True = evil url
def urlcompare(url):
	file_count = 0
	for i in os.listdir('./blacklists'):
		if os.path.isdir('./blacklists' + '/' + i):
			for j in os.listdir('./blacklists' + '/' + i):
				with open('./blacklists' + '/' + i + '/' + j) as f:
					for line in f:
						file_count = file_count + 1
						if url == line[:-1]:
							return True
	return False

if __name__ == '__main__':
	inBlacklist = urlcompare(url)
	


