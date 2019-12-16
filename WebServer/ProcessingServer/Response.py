#_*_ coding:utf-8 _*_
import time

from http import HTTPStatus
import httpr.HttpHeader

class Response(object):
    def __init__(self, request, application):
        self.request = request
        self.application = application

        self.headersParameter = None

    def __call__(self):
        if self.request.yvan_isWOF:
            environ = self.request.retEnviron()
            body = self.application(environ, self.start_response)
            if body == None:
                status = HTTPStatus.INTERNAL_SERVER_ERROR
                header = "HTTP/1.1 %s %s\r\n" %(status.value, status.phrase)
            else:
                status, headers = self.headerParameter
                header = "HTTP/1.1 %s\r\n" % status
        else:
            flag, body = self.SFRead(self.request.PATH_INFO)
            
            if flag == False:
                status = HTTPStatus.NOT_FOUND
            else:
                status = HTTPStatus.OK

            content_type = ("Content-Type", self.request.yvan_mimetype)
            if self.request.yvan_mimetype == "text/html":
                content_type = ("Content-Type", "text/html; charset=utf-8")
            if flag == False and self.request.yvan_mimetype == "text/html":
                status = HTTPStatus.NOT_FOUND
                flag, body = self.SFRead('/404.html')
                    
            header = "HTTP/1.1 %s %s\r\n" %(status.value, status.phrase)
            headers = {
                ("Cache-Control" ,"%s" %httpr.HttpHeader.Cache_Control.NO_CACHE.value),
                ("Connection", "%s" %httpr.HttpHeader.Connection.CLOSE.value),
                ("X-Frame-Options", "%s" %httpr.HttpHeader.X_Frame_Options.SAMEORIGIN.value),
                }
            headers.add(content_type)

        if headers != None:
            for item in headers:
                header += "%s: %s\r\n" %(item[0], item[1])
        header += "%s\r\n" %self.GetServrtData()
        header += "Server: %s\r\n" %self.request.server_version
        header += "\r\n"
        
        # 针对HEAD方法进行响应
        if self.request.REQUEST_METHOD.upper() == 'HEAD':
            body = ''

        if type(body) != bytes:
            body = body.encode(httpr.HttpHeader.Encoding.UTF_8.value)

        if type(header) != bytes:
            header = header.encode(httpr.HttpHeader.Encoding.UTF_8.value)
        print('=====>')
        print(body)
        print('<=End')
        context = (header, body)
        return context

    def start_response(self, status, headers, exc_info = None):
        self.headerParameter = status, headers

    def SFRead(self, path):
        try: 
            file_path = self.request.static_path + path
            print(file_path)
            fResp = open(file_path, "rb")
            docontent = fResp.read()
            fResp.close()
            flag = True
        except:
            docontent = ''
            flag = False
        finally:
            return flag, docontent

    @staticmethod
    def GetServrtData():
        # Date: Sun, 17 Feb 2019 10:37:46 GMT
        return time.strftime("Date: %a, %d %b %Y %H:%M:%S GMT", time.gmtime())


