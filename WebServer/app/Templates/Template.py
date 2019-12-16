import logging
import re

class Template(object):
    def __init__(self, folder):
        self.templates = "./app/Templates/"
        self.AppTemplafolder = folder

    def readTemplateFile(self, templateFile):
        path = self.templates + self.AppTemplafolder + templateFile
        try:
            with open(path) as f:
                template = f.read()
        except Exception as identifier:
            logging.warning(identifier)
        return template
            
    def templateProcess(self, template, parameterDir):
        items = parameterDir.items()
        content = template
        if len(items) > 0:
            for key, value in items:
                key = '@{%s}' %key
                print('%s ----> %s' %(key, value))
                content = re.sub(key, value, content)
        return content

    def retContent(self, templateFile, parameterDir):
        return self.templateProcess(self.readTemplateFile(templateFile), parameterDir)
