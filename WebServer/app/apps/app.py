#_*_ coding:utf-8 _*_

class ApplicationController(object):
    def __init__(self):
        self.application_s = {}

    def addApplication(self, applications):
        self.application_s.update(applications)

    def run(self, appUrl):
        print(self.application_s)
        view = self.application_s.get(appUrl, None) #bug 应该使用GET获取，并默认返回debug页
        return view.run()

