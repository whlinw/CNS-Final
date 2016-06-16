from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

httpd = HTTPServer(('140.112.30.32', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, keyfile="./domain.key", certfile='./domain.crt', server_side=True)

httpd.serve_forever()
