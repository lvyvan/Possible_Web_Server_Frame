#_*_ coding:utf-8 _*_
import urllib.parse

import possible.Context.Cookie
import possible.Context.Session

class HttpRequest(object):
    def __init__(self, environ, start_response):
        if environ == None:
            return None
        self.environ = environ
        self.start_response = start_response
        
        self.REQUEST_METHOD = self.environ['REQUEST_METHOD']         # 请求方法
        self.SCRIPT_NAME = self.environ['SCRIPT_NAME']               # 应用程序对象
        self.PATH_INFO = self.environ['PATH_INFO']                   # 请求目标的虚拟“位置”
        self.QUERY_STRING = self.environ['QUERY_STRING']             # URL中 "?" 后面的部分
        self.CONTENT_TYPE = self.environ['CONTENT_TYPE']
        self.CONTENT_LENGTH = self.environ['CONTENT_LENGTH']
        self.SERVER_NAME = self.environ['SERVER_NAME']               # 服务器名
        self.SERVER_PORT = self.environ['SERVER_PORT']               # 端口
        self.SERVER_PROTOCOL = self.environ['SERVER_PROTOCOL']       # HTTP / 1.1

        self.wsgi_version = self.environ['wsgi.version']             # 元组(1,0)
        self.wsgi_url_scheme = self.environ['wsgi.url_scheme']       # http / https
        self.wsgi_input = self.environ['wsgi.input']                 # http 正文流
        self.wsgi_errors = self.environ['wsgi.errors']               # 错误流
        self.wsgi_multithread = self.environ['wsgi.multithread']     # 线程调用
        self.wsgi_multiprocess = self.environ['wsgi.multiprocess']   # 进程调用
        self.wsgi_run_once = self.environ['wsgi.run_once']           # 一次调用的网关期望 

        self.Possible_appUrl, self.Possible_rout = self.getAppUrl_rout()

        self.Possible_request_parameter = {}

        # 处理HTTP_
        for key, value in self.environ.items():
            if 'HTTP_' in key:
                setattr(self, key, value)
        # list
        self.environ_items = self.environ.keys()
        
        sessionid = None
        # Cookie对象
        self.Cookie = possible.Context.Cookie.Cookie()
        
        cookie_str = self.GetAttributes('HTTP_COOKIE')
        if cookie_str != None:
            self.Cookie.CookieLoad(cookie_str)
            sessionid = self.Cookie.GetCookie("sessionid")

        # session
        self.Session = possible.Context.Session.Session(self.SERVER_NAME)
        self.Session.CreateSession(sessionid)

        if self.REQUEST_METHOD == 'POST':
            if self.CONTENT_TYPE != None:
                if '; ' in self.CONTENT_TYPE:
                    media_type, attach = self.CONTENT_TYPE.split('; ', 1)
                    if media_type == 'application/x-www-form-urlencoded':
                        if '&' in self.wsgi_input:
                            list = self.wsgi_input.split('&')
                            for item in list:
                                key, value = item.split('=', 1)
                                self.Possible_request_parameter[key] = value
                        else:
                            key, value = self.wsgi_input.split('=', 1)
                    elif media_type == '':
                        # 处理上传文件
                        pass
                        

    def GetAttributes(self, key, default = None):
        key = key.upper()
        return getattr(self, key, default)

    def getAppUrl_rout(self):
        if self.PATH_INFO == '/':
            self.PATH_INFO = '/index'
        if '/' in self.PATH_INFO:
            urlList = self.PATH_INFO.split("/", 2)
        if len(urlList) == 2:
            appUrl, rout = urlList
        else:
            sp, appUrl, rout = urlList
        return appUrl, rout

    @property
    def UserHostAddress(self, host = True):
        '''
            获得服务器名或IP
            host = True -> return HTTP_HOST
            host = False -> SERVER_NAME/IP
        '''
        if host == True:
            host, port = self.GetAttributes('HTTP_HOST').split(':', 1)
        else:
            host, port = (self.SERVER_NAME, self.SERVER_PORT)
        return host, port

    @property
    def Url(self):
        return self.PATH_INFO