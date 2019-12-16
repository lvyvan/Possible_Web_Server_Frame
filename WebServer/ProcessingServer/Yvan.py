#_*_ coding:utf-8 _*_
import ProcessingServer.Request
import ProcessingServer.Response

from http import HTTPStatus

class YvanServer(object):
    def __init__(self, respServerSocket, client_addr, static_path, application, server_version):
        self.respServerSocket = respServerSocket
        self.client_addr = client_addr
        self.static_path = static_path
        self.application = application
        self.server_version = server_version

    def run(self):
        request = ProcessingServer.Request.Request(self.respServerSocket, self.client_addr, self.static_path, self.server_version)
        if request != None:
            response = ProcessingServer.Response.Response(request, self.application)
            content = response()
        else:
            content == None
        return content




