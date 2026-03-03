"""Simple HTTP server that serves static files."""
import os
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main() -> None:
    port = int(os.environ.get("PORT", "3000"))
    directory = os.path.join(os.path.dirname(__file__), "static")
    handler = partial(SimpleHTTPRequestHandler, directory=directory)
    server = HTTPServer(("0.0.0.0", port), handler)
    print(f"Serving on http://0.0.0.0:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
