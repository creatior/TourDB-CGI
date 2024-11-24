from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

base_url = ("localhost", 8000)
http_server = HTTPServer(base_url, CGIHTTPRequestHandler)
http_server.serve_forever()