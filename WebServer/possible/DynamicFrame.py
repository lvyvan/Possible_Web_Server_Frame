# _*_ coding:utf-8 _*_
from app.apps.app import ApplicationController
from possible.Context.Context import Context

from app.Controller.Home.Home import Home


class DynamicFramework(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def run(self):
        context = Context(self.environ, self.start_response)
        if context == None:
            return None

        appCon = ApplicationController()
        # 注册应用
        appCon.addApplication({
            '': Home(context),
            'user': '',
        })
        return appCon.run(context.Request.Possible_appUrl)
