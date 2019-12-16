# _*_ coding:utf-8 _*_
import mimetypes
import os.path
from http import HTTPStatus

import httpr.HttpHeader 


class HttpResponse(object):
    def __init__(self, Request):
        self.Request = Request

        self.x_Frame_Options = httpr.HttpHeader.X_Frame_Options.SAMEORIGIN.value
        self.cache_Control = httpr.HttpHeader.Cache_Control.MAX_AGE_120.value
        self.connection = httpr.HttpHeader.Connection.KEEP_ALIVE.value
        self.httpStatus = None
        self.Set_HttpStatus(HTTPStatus.OK)
        self.content_Type = 'text/html; charset=%s' %httpr.HttpHeader.Encoding.UTF_8.value
        self.buffer = ''
        self.referer = None
        self.stream_bytes = bytes

    def Set_HttpStatus(self, hs: HTTPStatus):
        self.httpStatus = "%s %s" % (hs.value, hs.phrase)

    def Set_X_Frame_Options(self, xfo: httpr.HttpHeader.X_Frame_Options):
        self.x_Frame_Options = xfo.value

    def Set_Cache_Control(self, cc: httpr.HttpHeader.Cache_Control):
        self.cache_Control == cc.value

    def Set_Connection(self, con: httpr.HttpHeader.Connection):
        self.connection = con.value

    def Set_Content_Type(self, filePath, isBinary: bool = False):
        mimeType = mimetypes.guess_type(filePath)[0]
        if mimeType == None:
            if isBinary == True:
                mimeType = 'application/octet-stream'
            else:
                mimeType = 'text/plain'
        if mimeType == 'text/html':
            mimeType = "%s; charset=%s" %(mimeType, httpr.HttpHeader.Encoding.UTF_8.value)
        self.content_Type = mimeType

    def retResponseHeader(self):
        headerSet = {
            ('X-Frame-Options', self.x_Frame_Options),
            ('Cache-Control', self.cache_Control),
            ('Connection', self.connection),
            ('Content-Type', self.content_Type),
        }
        if self.referer != None:
            headerSet.union({("Referer", self.referer), })
        return headerSet

    def Set_Cookie4Session(self):
        self.Request.Cookie.sCookie["sessionid"] = self.Request.Session.sessionid
        self.Request.Cookie.sCookie["sessionid"]["path"] = "/"
        return self.Request.Cookie.RetCookie()

    def Write(self, content):
        if type(content) == bytes:
            self.buffer = content
        else:
            self.buffer += content

    def Buffer_Clear(self):
        self.buffer = ''

    def End(self):
        '''-> run'''
        self.run()

    def Redirect(self, URL):
        '''-> run'''
        self.referer = URL
        self.run()

    def run(self):
        headerSet = self.retResponseHeader()
        if 'text' in self.content_Type:
            headerSet = headerSet.union(self.Set_Cookie4Session())

        self.Request.start_response(self.httpStatus, headerSet)
        content = self.buffer
        print(self.content_Type)
        if type(content) != bytes:
            content = content.encode(httpr.HttpHeader.Encoding.UTF_8.value)
        return content

