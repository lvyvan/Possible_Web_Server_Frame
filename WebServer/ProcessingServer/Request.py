#_*_ coding:utf-8 _*_

import socket
import mimetypes

from urllib import parse

class Request(object):
    def __init__(self, respServerSocket, client_addr, static_path, server_version):
        self.respServerSocket = respServerSocket

        self.requestByte = respServerSocket.recv(1024)
        self.static_path = static_path
        self.server_version = server_version

        if not self.requestByte:    #防空
            return None

        self.requestStr = self.requestByte.decode("utf-8")
        print(self.requestStr)

        self.REQUEST_METHOD = None      # 请求方法
        self.SCRIPT_NAME = None         # 应用程序对象
        self.PATH_INFO = None           # 请求目标的虚拟“位置”
        self.QUERY_STRING = None        # URL中 "?" 后面的部分
        self.CONTENT_TYPE = None
        self.CONTENT_LENGTH = None      #
        self.SERVER_NAME = client_addr  # 服务器名
        self.SERVER_PORT = None         # 端口
        self.SERVER_PROTOCOL = None     # HTTP / 1.1
        self.wsgi_version = (1, 0)      # 元组(1,0)
        self.wsgi_url_scheme = 'http'   # http / https
        self.wsgi_input = None          # http正文流
        self.wsgi_errors = None         # 错误流
        self.wsgi_multithread = False   # 线程调用
        self.wsgi_multiprocess = False  # 进程调用
        self.wsgi_run_once = True       # 一次调用的网关期望 

        # Yvan_*_s 服务器
        self.yvan_isWOF = None                  # 是否动态文件
        self.yvan_static_path = static_path     # 静态文件目录
        self.yvan_mimetype = None              # 请求文件的文件类型 mimetype

        # HTTP_ Variable_s                                   +
        self.HTTP_Variables_dic = {}
        # 对应于客户端提供的HTTP请求标头的变量(即名称以“HTTP_”开头的变量)
        # 这些变量的存在与否应与请求中是否存在适当的HTTP头相对应

        ip, self.SERVER_PORT = self.respServerSocket.getpeername()

        if '\r\n\r\n' in self.requestStr:
            header, body = self.requestStr.split('\r\n\r\n', 1)
        else:
            header, body = (self.requestStr, "")

        request_list = header.splitlines()
        self.REQUEST_METHOD, url, self.SERVER_PROTOCOL  = request_list.pop(0).split(' ')  # 请求方式，url, Http版本
        
        # 限制请求方法
        method = self.REQUEST_METHOD.upper()
        if  (method != 'GET' and method != 'POST' and method != 'HEAD'):
            return None

        urlparse = parse.urlparse(url)
        self.PATH_INFO, self.QUERY_STRING = urlparse.path, urlparse.query
        '''
            None
            ('text/html', None)
        '''
        mimetype_s = mimetypes.guess_type(self.PATH_INFO)[0]
        if mimetype_s == None:
            self.yvan_isWOF = True
        else:
            self.yvan_mimetype = mimetype_s
            self.yvan_isWOF = False

        for item in request_list:
            if item != '':
                key, value = item.split(': ')
                key = 'HTTP_%s' %key.upper().replace('-', '_')
                setattr(self, key, value)   # 生成属性
                self.HTTP_Variables_dic[key] = value

        self.CONTENT_TYPE = getattr(self, 'HTTP_CONTENT_TYPE', None)
        self.CONTENT_LENGTH = getattr(self, 'HTTP_CONTENT_LENGTN', None)

        if self.CONTENT_LENGTH != None:
            date_len = 1024
            size = int(self.CONTENT_LENGTH) - 1024
            while size >= 0 or date_len > 0:
                data = respServerSocket.recv(1024, socket.MSG_WAITALL)
                date_len = len(data)
                self.requestByte += data
                size -= date_len

            if int(self.CONTENT_LENGTH) > 1024:
                self.requestStr = self.requestByte.decode('utf-8')
                header, body = self.requestStr.split('\r\n\r\n', 1)

        self.wsgi_input = body

        # ---- debug --------
        print(self.PATH_INFO)
        print(self.HTTP_Variables_dic)
        print(mimetype_s)
        print('------input-----')
        print(self.wsgi_input)
        print('------end input------')
        print(self.yvan_isWOF)
        # ---- end debug --------

    def retEnviron(self):
        environ = dict()
        environ['REQUEST_METHOD'] = self.REQUEST_METHOD
        environ['SCRIPT_NAME'] = self.SCRIPT_NAME
        environ['PATH_INFO'] = self.PATH_INFO
        environ['QUERY_STRING'] = self.QUERY_STRING
        environ['CONTENT_TYPE'] = self.CONTENT_TYPE
        environ['CONTENT_LENGTH'] = self.CONTENT_LENGTH
        environ['SERVER_NAME'] = self.SERVER_NAME
        environ['SERVER_PORT'] = self.SERVER_PORT
        environ['SERVER_PROTOCOL'] = self.SERVER_PROTOCOL
        # HTTP_ Variables
        # 对应于客户端提供的HTTP请求标头的变量（即名称以“HTTP_”开头的变量）。 
        # 这些变量的存在与否应与请求中是否存在适当的HTTP头相对应
        environ.update(self.HTTP_Variables_dic)

        environ['wsgi.version'] = self.wsgi_version
        environ['wsgi.url_scheme'] = self.wsgi_url_scheme
        environ['wsgi.input'] = self.wsgi_input
        environ['wsgi.errors'] = self.wsgi_errors
        environ['wsgi.multithread'] = self.wsgi_multithread
        environ['wsgi.multiprocess'] = self.wsgi_multiprocess
        environ['wsgi.run_once'] = self.wsgi_run_once
        return environ


        

        
            

        

        





        


        