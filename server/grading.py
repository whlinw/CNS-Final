import ssllabsscanner
import sys
import socket
import ssl
import signal
# import urllib2
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

pref_order = ['ECDHE-RSA-AES256-GCM-SHA384', 'ECDHE-ECDSA-AES256-GCM-SHA384', 'ECDHE-RSA-AES256-SHA384', 
'ECDHE-ECDSA-AES256-SHA384', 'ECDHE-RSA-AES256-SHA', 'ECDHE-ECDSA-AES256-SHA', 'DHE-DSS-AES256-GCM-SHA384', 
'DHE-RSA-AES256-GCM-SHA384', 'DHE-RSA-AES256-SHA256', 'DHE-DSS-AES256-SHA256', 'DHE-RSA-AES256-SHA', 'DHE-DSS-AES256-SHA', 
'AES256-GCM-SHA384', 'AES256-SHA256', 'AES256-SHA', 'ECDHE-RSA-AES128-GCM-SHA256', 'ECDHE-ECDSA-AES128-GCM-SHA256', 
'ECDHE-RSA-AES128-SHA256', 'ECDHE-ECDSA-AES128-SHA256', 'ECDHE-RSA-AES128-SHA', 'ECDHE-ECDSA-AES128-SHA', 'DHE-DSS-AES128-GCM-SHA256',
 'DHE-RSA-AES128-GCM-SHA256', 'DHE-RSA-AES128-SHA256', 'DHE-DSS-AES128-SHA256', 'DHE-RSA-AES128-SHA', 'DHE-DSS-AES128-SHA', 
 'AES128-GCM-SHA256', 'AES128-SHA256', 'AES128-SHA']

def alarm(time):
	def handler(signum, frame):
		return 'Timeout'
		exit()
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(time)
def grading(url):
	try:
	    urlopen(url)
	except HTTPError as e:
		#print e.code, '1'
		return 'HTTP Error'
	except URLError as e:
		#print e.args, '2'
		return 'Invalid URL'

	alarm(5)
	bad = 0
	if url[:5] != 'https':
		bad = 1
	# return sys.argv[1]
	data = ssllabsscanner.resultsFromCache(url)
	score = 0

	if 'endpoints' in data and 'grade' in data['endpoints'][0]:
		# print type(data['endpoints'][0]['grade'])
		return chr(ord(str(data['endpoints'][0]['grade'])) + bad)
	else:
		# return "GG"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ssl_sock = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED,ca_certs=None)
		ssl_sock.connect((url,443))
		wanted = ssl_sock.cipher()[0]
		score = 100 - (float(100) / len(pref_order)) * pref_order.index(wanted)
		

		if pref_order.index(wanted) < 6:
			grade = 'A'
 
		elif pref_order.index(wanted) < 12:
			grade = 'B'
		
		elif pref_order.index(wanted) < 18:
			grade = 'C'

		if ssl_sock.version()[:5] != 'TLSv1':
			grade += 1

		return chr(ord(grade) + bad)

if __name__ == '__main__':
	result = grading(sys.argv[1])
	print(result)



# data = ssllabsscanner.newScan(sys.argv[1])
# return(data['endpoints'][0]['grade'])

