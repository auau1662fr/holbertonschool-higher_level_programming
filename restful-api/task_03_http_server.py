#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_headers(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._send_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            data = {"status": "OK"}
            self._send_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/info":
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            data = {"error": "Endpoint not found"}
            self._send_headers(404)
            self.wfile.write(json.dumps(data).encode())

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
