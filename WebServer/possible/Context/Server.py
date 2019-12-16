#_*_ coding:utf-8 _*_
import os.path
import urllib.parse

class Server(object):
    def __init__(self):
        pass

    def RelPath(self, path):
        '''绝对路径转相对路径'''
        return os.path.relpath(path)

    def MapPath(self, path):
        '''获取文件的绝对路径，相对路径转绝对路径'''
        return os.path.abspath(path)

    def HtmlEncode(self, html):
        '''编码'''
        return html.encode("utf-8")

    def HtmlDeCode(self, html):
        '''解码'''
        return html.decode("utf-8")

    def UrlEncode(self, urlStr):
        '''url 编码'''
        return urllib.parse.quote(urlStr)

    def UrlDecode(self, urlStr):
        '''url 解码'''
        return urllib.parse.unquote(urlStr)
        

def main():
    pass

if __name__ == "__main__":
    main()
