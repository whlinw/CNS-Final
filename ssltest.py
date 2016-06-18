import ssl
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED,ca_certs=None)
ssl_sock.connect((sys.argv[1],443))
# print repr(ssl_sock.getpeername())
print ssl_sock.version()
print ssl_sock.cipher()
