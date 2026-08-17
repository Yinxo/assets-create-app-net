"""Lokaler Hausideen-Server MIT no-cache Headern.

Der eingebaute `python -m http.server` sendet keine Cache-Control-Header, darum
cachen (v.a. TV-)Browser die index.html heuristisch als "frisch" und laden neuen
Code nie nach — nur data.json (die vom Client cache-frei geholt wird) kommt durch.
Dieser Server schickt `Cache-Control: no-store` auf ALLE Antworten, damit jeder
Reload garantiert die aktuelle index.html/JS bekommt. Bilder aendern ihren Namen
bei Ersetzung, sind also ohnehin cache-sicher.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 4012


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    # If-Modified-Since ignorieren -> nie 304, immer frischer Inhalt.
    def send_head(self):
        if "If-Modified-Since" in self.headers:
            del self.headers["If-Modified-Since"]
        if "If-None-Match" in self.headers:
            del self.headers["If-None-Match"]
        return super().send_head()


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", PORT), NoCacheHandler) as httpd:
        httpd.serve_forever()
