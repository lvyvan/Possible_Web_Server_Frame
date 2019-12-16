#_*_ coding:utf-8 _*_
import time
import logging

import possible.Context.Cache
import possible.Context.HttpRequest
import possible.Context.HttpResponse
import possible.Context.Cache
import possible.Context.Server

class Context(object):
    def __init__(self, environ, start_response):
        self.Request = possible.Context.HttpRequest.HttpRequest(environ, start_response)
        if self.Request == None:
            return None
        self.Response = possible.Context.HttpResponse.HttpResponse(self.Request)
        self.Cacha = possible.Context.Cache.Cache()
        self.Server = possible.Context.Server.Server()
        self.Tag = None


