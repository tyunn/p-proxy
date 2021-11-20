import urllib.parse
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler
import urllib.request

PORT = 8002
TARGER_DOMAIN = 'http://news.ycombinator.com'


class MyProxy(SimpleHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.end_headers()
        full_url = urllib.parse.urljoin(TARGER_DOMAIN, self.path)
        print(full_url)

        self.copyfile(urllib.request.urlopen(full_url), self.wfile)


class ReuseAddressTCPServer(TCPServer):
    allow_reuse_address = True


def main():
    with ReuseAddressTCPServer(('', PORT), MyProxy) as httpd:
        print("Now serving at" + str(PORT))
        httpd.serve_forever()


if __name__ == '__main__':
    main()
