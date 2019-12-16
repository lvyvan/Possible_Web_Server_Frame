#_*_ coding:utf-8 _*_
import multiprocessing
import re
import socket
import time

import ProcessingServer.Response
import ProcessingServer.Request
import ProcessingServer.Yvan

class Server(object):
    def __init__(self, initDic):
        self.port = initDic["port"]
        self.application = initDic["applic"]
        self.static_path = initDic["static_path"]
        self.server_version = initDic["server_version"]
        # 设置TCP
        self.tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpServerSocket.bind(("", self.port))
        self.tcpServerSocket.listen(128)

    def runServrt(self):
        while True:
            respServerSocket, client_addr = self.tcpServerSocket.accept()
            proc = multiprocessing.Process(target=self.serverClient, args=(respServerSocket, client_addr, ))
            proc.start()
            """
            是因为windows操作系统的原因，在Windows中，多进程multiprocessing使用的是序列化pickle来在多进程之间转移数据，
            而socket对象是不能被序列化的，但是在linux操作系统上却没问题，因为在linux上多进程multiprocessing使用的是fork，所以在windows上可以改用多线程。
            因为网络通信属于io密集型的操作，对cpu计算要求不高，不用多进程，用多线程就行。
            """
            respServerSocket.close()
        self.tcpServerSocket.close()

    def serverClient(self, respServerSocket, client_addr):
        yvanServer = ProcessingServer.Yvan.YvanServer(respServerSocket, client_addr, self.static_path, self.application, self.server_version)
        context = yvanServer.run()
        if context != None:
            header, body = context
            respServerSocket.send(header)
            respServerSocket.send(body)
        respServerSocket.close()
