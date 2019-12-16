#_*_ coding:utf-8 _*_
import logging  
from possible.DynamicFrame import DynamicFramework

def application(environ, start_response):
    df = DynamicFramework(environ, start_response)
    if df == None:
        return None
    return df.run()