from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer

# class SimpleHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(b'Hello, World!')

class WebPageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Welcome to the Home Page!</h1>')
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>About Us</h1><p>We are a company specializing in web development.</p>')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Page Not Found</h1><p>The requested page does not exist.</p>')

server = TCPServer(('localhost', 8000), WebPageHandler)
server.serve_forever()

# server = TCPServer(('localhost', 8000), SimpleHandler)
# server.serve_forever()
