# query: www.google.com/search?q=URL
# # results: <div id="resultStats">
# result title: <h3 class="r">
# result description: <span class="st">
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

GWS = 'https://www.google.com/search?q='

def get_result(url):
	q = GWS + url
	req = Request(q)
	req.add_header("User-Agent", "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11")
	res = urlopen(req).read()
	return res

def search(url):
	html = get_result(url)
	parsed_html = BeautifulSoup(html, 'lxml')
	num = parsed_html.body.find('div', attrs={'id':'resultStats'}).text.split()[1]
	title = parsed_html.body.find('h3', attrs={'class':'r'}).text
	content = ' '.join(parsed_html.body.find('span', attrs={'class':'st'}).text.split('\n'))
	return num, title, content

if __name__ == '__main__':
	url = input('insert URL:')
	n, t, c = search(url)
	print(n, t, c)