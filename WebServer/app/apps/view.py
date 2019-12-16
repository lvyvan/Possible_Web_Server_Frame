#_*_ coding:utf-8 _*_
import re
import logging

from possible.Context import Context

class View(object):
    def __init__(self, context):
        self.context = context
        self.routDic = {}

    def AddRout(self, rout, func):
        self.routDic[rout] = func

    def AddRoutDic(self, routs):
        self.routDic.update(routs)

    def run(self):
        for route, func in self.routDic.items():
            result = re.match(route, self.context.Request.Possible_rout)
            if result:
                context = func(self.context, result)
                if context != None:
                    self.context.Response.Write(context)
                break
        else:
            print('-----Error Path-----')
            print(self.context.Request.PATH_INFO)
            print('-----END Path-------')
            # 错误处理
        return self.context.Response.run()