from http.server import BaseHTTPRequestHandler,HTTPServer

port=9000
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200);
        self.send_header('Content_Type','text/html:charset=utf-8')
        print('recive request')
        self.end_headers()
        self.wfile.write('<h1>Hello World\n</h1>'.encode('utf-8'))

#서버구동
httpd=HTTPServer(('',9000),MyHTTPRequestHandler)
print('HTTP Server Starts...')
httpd.serve_forever()