# task_03_http_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="text/plain"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            # Page d'accueil simple
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            # Retourne un JSON
            self._set_headers(content_type="application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            # Endpoint status
            self._set_headers(content_type="application/json")
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))
        else:
            # Endpoint inconnu -> 404
            self._set_headers(404, "application/json")
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
