#!/usr/bin/python
#-*- coding:utf-8 -*-
#
# Author: ye.zhiqin@outlook.com
# Date  : 2016/11/30

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from sms_sender import SmsSender
import urllib

PORT_NUMBER = 4001

#This class will handles any incoming request
class SMSProvider(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("It Works!")
        return

    #Handler for the POST requests
    def do_POST(self):
        if self.path=="/sender/sms":
            try:
                #start to process falcon post request
                data = self.rfile.read(int(self.headers['content-length']))
                sms = urllib.unquote(data)

                #send message
                sender = SmsSender(sms)
                status = sender.send()

                #send response
                self.send_response(200)
                self.end_headers()
                self.wfile.write("success")
                return      
            except:
                self.send_response(200)
                self.end_headers()
                self.wfile.write("error")
                return      
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Request must be posted to http://ip:port/sender/sms!")
            return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), SMSProvider)
    print 'Started httpserver on port %s' % PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except:
    print 'Shutting down the web server'
    server.socket.close()
