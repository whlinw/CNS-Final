from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import urllib.parse as urlparse
import http.client as httplib
import json
from urlcompare import urlcompare
from search import search
from makeHTML import makeHTML
from grading import grading

HOST = '140.112.30.39'
PORT = 4443

# List of URL shorten service
USS = ['goo.gl', 'bit.ly', 'ppt.cc', 'tinyurl.com', '0rz.tw', 'ow.ly']

class requestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		# res = []
		res = {}

		if parsed_path.path == '/analyze':
			url = parsed_path.query.split('=')[1]
			while isShorten(url) == True:
				_, url = get(url)
			res['url'] = url
			prot, domain, path = parseURL(url)
			res['evil'] = str(urlcompare(domain))
			num, title, content = search(url)
			res['num'] = num
			res['title'] = title
			res['content'] = content
			res['grade'] = grading(url)
		elif parsed_path.path == '/expand':
			url = parsed_path.query.split('=')[1]
			while isShorten(url) == True:
				_, url = get(url)
			res['url'] = url
		elif parsed_path.path == '/check':
			url = parsed_path.query.split('=')[1]
			_, domain, _=parseURL(url)
			res['evil'] = str(urlcompare(domain))
		elif parsed_path.path == '/grade':
			url = parsed_path.query.split('=')[1]
			while isShorten(url) == True:
				_, url = get(url)
			print('URL:', url)
			grade = grading(url)
			res['grade'] = grade
			print('Grade:', grade)
		elif parsed_path.path == '/search':
			url = parsed_path.query.split('=')[1]
			num, title, content = search(url)
			res['num'] = num
			res['title'] = title
			res['content'] = content
			# print('Content:', content.decode('utf-8'))
		
		self.send_response(200)
		self.end_headers()
		result = makeHTML(json.dumps(res))
		self.wfile.write(result.encode('utf-8'))
		return

def parseURL(url):
	if url.find('://') != -1:
		protocol = url[0:url.find('://')]
		path = url[url.find('://')+3:]
	else:
		protocol = 'http'
		path = url

	if path.find('/') != -1:
		host = path[:path.find('/')]
		path = path[path.find('/'):]
	else:
		host = path
		path = '/'
	return protocol, host, path

def get(url):
	prot, host, path = parseURL(url)
	if prot == 'https':
		conn = httplib.HTTPSConnection(host)
	else:
		conn = httplib.HTTPConnection(host)
	conn.request('GET', path)
	res = conn.getresponse()
	code = int(res.status)
	if code//100 == 3:
		locat = res.getheader('Location')
	else:
		locat = 'None'

	print(code, 'GET', url, locat)
	return code, locat

def isShorten(url):
	prot, host, path = parseURL(url)
	if host in USS:
		return True
	else:
		return False

def run():
	httpd = HTTPServer((HOST, PORT), requestHandler)
	httpd.socket = ssl.wrap_socket (httpd.socket, keyfile="./domain.key", certfile='./domain.crt', server_side=True)
	print('* Running on', httpd.server_address[0] + ':' + str(httpd.server_address[1]), '(Press CTRL+C to quit)')
	httpd.serve_forever()

if __name__ == '__main__':
	run()
