#_*_ coding:utf-8 _*_
import logging
import sys

import ProcessingServer.InitServer
import ProcessingServer.Httpd


def InitLogger():
    logger = logging.getLogger()  
    logger.setLevel(logging.INFO)   
    logfile = './log.log'  
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.DEBUG)   
    ch = logging.StreamHandler()  
    ch.setLevel(logging.WARNING)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh) 
    logger.addHandler(ch)

def main():
    InitLogger()
    init = ProcessingServer.InitServer.Init()
    if init.runInit() == False:
        return
    server = ProcessingServer.Httpd.Server(init.RetConfDirc())
    server.runServrt()
    
if __name__ == "__main__":
    main()
