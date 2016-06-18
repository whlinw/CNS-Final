import ssllabsscanner
import sys
import socket
import ssl
import signal



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
	alarm(5)

	# return sys.argv[1]
	data = ssllabsscanner.resultsFromCache(sys.argv[1])

	score = 0

	if 'endpoints' in data and 'grade' in data['endpoints'][0]:
		return (data['endpoints'][0]['grade'])
	else:
		# return "GG"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ssl_sock = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED,ca_certs=None)
		ssl_sock.connect((sys.argv[1],443))
		wanted = ssl_sock.cipher()[0]
		score = 100 - (float(100) / len(pref_order)) * pref_order.index(wanted)
		if ssl_sock.version()[:5] != 'TLSv1':
			return 'F'

		elif pref_order.index(wanted) < 6:
			return 'A'

		elif pref_order.index(wanted) < 12:
			return 'B'
		
		elif pref_order.index(wanted) < 26:
			return 'C'
		else:
			return 'D'
if __name__ == '__main__':
	result = grading(sys.argv[1])
	print result



# data = ssllabsscanner.newScan(sys.argv[1])
# return(data['endpoints'][0]['grade'])

