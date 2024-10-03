# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

Class MYHandler(SimpleHTTPRequestHandler):
     def do_Get(self):
        self.send_response(200)
        self.sendsend_header('Content-type' , 'text/htal')
        self.end_headers()
        self.wfile.write(b'HELLO,WORLD?? MY NAME IS CHIITI MEMORY  2TERA BYTE .THIS IS MY PYTHON APPLICATION APP')
httpd = HTTPServer (('',PORT),MYHandler)
print(f'Sering on port {PORT}...')
http.server_forever()
