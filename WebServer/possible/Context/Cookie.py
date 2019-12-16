#_*_ coding:utf-8 _*_
import http.cookies

class Cookie(object):
    def __init__(self):
        self.sCookie = http.cookies.SimpleCookie()
        self.reqCookieDic = {}

    def CookieLoad(self, rewdata):
        if rewdata == "" or rewdata == None:
            return
        cTeList = []
        if ';' in rewdata:
            cTeList = rewdata.split('; ')
        else:
            cTeList.append(rewdata)
        for item in cTeList:
            key, value = item.split('=')
            self.reqCookieDic[key] = value

    def GetCookie(self, key):
        return self.reqCookieDic.get(key, None)

    def RetCookie(self):
        set_cookieList = self.sCookie.output().splitlines()
        ret = set()
        for item in set_cookieList:
            key, value = item.split(': ')
            ret.add((key, value))
        return ret

def main():
    c = Cookie()
    #sessionid=88245be7fbf549c13b42075d; check="gAAAAABcpfvM8KrsntMb4jxihY="; user=gAAAAABcpfv7B_pfTcuWFvCPUs60
    c.CookieLoad("sessionid=88245be7fbf549c13b42075d; check=gAAAAABcpfvM8KrsntMb4jxihY=; user=gAAAAABcpfv7B_pfTcuWFvCPUs60")
    print(c.reqCookieDic)
    print(c.GetCookie("sessionid"))
'''
    c.sCookie["sessionid"] = "1111111"
    c.sCookie["sessionid"]["path"] = "/"
    c.sCookie["222"] = "22222222"
    c.sCookie["222"]["path"] = "/"
    c.sCookie["222"]['max-age'] = 123
    print(c.RetCookie())
    expires         #   日期字符串 指定过期时间
    path            #   匹配路径
    comment         #   给服务器说明如何使用该Cookie UTF-8
    domain          #   服务器只向指定的域名发送Cookie
    max-age         #   指定过期秒数
    secure          #   如果使用该属性，则只有在 Http SSL 安全连接时发送
    version         #   强制，对应Cookie版本 但没见人用过 :D
    httponly        #   cookie中设置了HttpOnly属性，那么通过js脚本将无法读取到cookie信息，这样能有效的防止XSS攻击

    from http import cookies
    c = cookies.SimpleCookie()
    c["supar"] = "netWork"
    c["supar"]["path"] = "/"
    c.output()
    'Set-Cookie: supar=netWork; Path=/'
    c["supar"]["max-age"] = "360"
    c.output()
    'Set-Cookie: supar=netWork; Max-Age=360; Path=/'
    c["supar"]["domain"] = "yvan.top"
    c.output()
    'Set-Cookie: supar=netWork; Domain=yvan.top; Max-Age=360; Path=/'
    '''

if __name__ == "__main__":
    main()
