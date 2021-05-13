import datetime
import http.server
import socketserver
import http.client
import pprint

# port = int(input("Введите порт: "))
# file = str(input("Введите файл: "))
d = []
err = "No errors"
count = 0

with open('data.txt', 'r') as f:
    d = f.read().splitlines()

port = int(d[0])

if len(d) > 1:
    file = str(d[1])
    a = file.find('.')
    type_file = file[a + 1:]
    if type_file != 'html':
        err = 'Error 403'
        file = 'error403.html'
else:
    err = 'Error 404'
    file = 'error404.html'


class ReqHand(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = ReqHand
with socketserver.TCPServer(("", port), handler) as httpd:
    a = ("Date: " + str(datetime.datetime.now()) +
         "\nPort: " + str(port) +
         "\nFile name: " + file +
         "\nErrors: " + str(err))
    print(a)

    # connection = http.client.HTTPSConnection("www.journaldev.com")
    # connection.request("GET", "/")
    # response = connection.getresponse()
    # headers = response.getheaders()
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint("Headers: {}".format(headers))

    httpd.serve_forever()
