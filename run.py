import re
import urllib.parse
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler
import requests
from bs4 import BeautifulSoup


# example url http://127.0.0.1:8002/item?id=13713480
WORD_LEN_TO_PROCESSING = 6
PORT = 8002
TARGER_DOMAIN = "http://news.ycombinator.com"


def replace_content(content: bytes) -> bytes:
    result = content
    soup = BeautifulSoup(content.decode("utf-8"), "html.parser")
    body = soup.body
    regex = re.compile(r"(\W)(\w{}{}{})(\W)".format(
        "{", WORD_LEN_TO_PROCESSING, "}"))

    for txt in body.find_all(string=True):
        if regex.search(txt) and txt.parent.name != "a":
            newtext = regex.sub(
                "{}{}{}".format(r"\1\2", u"\N{TRADE MARK SIGN}", r"\3"),
                txt,
            )
            txt.replace_with(newtext)
            result = soup.encode("utf-8")
    return result


class MyProxy(SimpleHTTPRequestHandler):
    def do_GET(self):
        full_url = urllib.parse.urljoin(TARGER_DOMAIN, self.path)
        r = requests.get(full_url)
        self.send_response(200)
        self.send_header("Content-type", r.headers["Content-Type"])
        self.end_headers()
        content = r.content

        if r.headers["Content-Type"].startswith("text/html"):
            content = replace_content(r.content)

        self.wfile.write(content)


class ReuseAddressTCPServer(TCPServer):
    allow_reuse_address = True


def main():
    with ReuseAddressTCPServer(("", PORT), MyProxy) as httpd:
        print("Now serving at" + str(PORT))
        httpd.serve_forever()


if __name__ == "__main__":
    main()
