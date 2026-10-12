#!/usr/bin/python3
"""Simple API built with Python's http.server module."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Request handler for the simple API."""

    def _send(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send(200, "text/plain", "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json", json.dumps(data))

        elif self.path == "/status":
            self._send(200, "text/plain", "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send(200, "application/json", json.dumps(info))

        else:
            self._send(404, "text/plain", "Endpoint not found")


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Serving on port {}...".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
