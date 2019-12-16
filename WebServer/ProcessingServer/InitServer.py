#_*_ coding:utf-8 _*_
import sys
import logging

class Init(object):
    def __init__(self):
        self.dynamic_path = None
        self.port = None    # int
        self.frames = None
        self.applics = None
        self.static_path = None
        self.serverVersion = None
        self.applic = None
        self.frame = None

    # 初始化
    def runInit(self):
        if self.loadConfig() == False:
            return False
        # 导入路径
        sys.path.append(self.dynamic_path)
        # 返回值标记导入模块
        self.frame = __import__(self.frames)
        # 此时app就指向了 dynamic/MiNiFrame模块中的application
        self.applic = getattr(self.frame, self.applics)
        return True

    # 读取配置文件
    def loadConfig(self):
        try:
            with open("./config/WebServer.conf", "r") as f:
                wsConf_info = eval(f.read())
            self.dynamic_path =wsConf_info["dynamic_path"] # 动态处理Frame
            self.port = int(wsConf_info["prot"])  # 监听端口
            self.frames = wsConf_info["frame"]    # 处理模块 Frame
            self.applics = wsConf_info["applic"]  # 接口函数
            self.static_path = wsConf_info["static_path"] # 静态文件位置
            self.serverVersion = wsConf_info["server_version"] # 服务器版本
            return True
        except Exception as identifier:
            print("[Error] as Loading Config Error! -> ", identifier)
            return False   

    # 返回读取信息Dirc
    def RetConfDirc(self):
        return {
            'dynamic_path': self.dynamic_path,
            'static_path': self.static_path,
            'port': self.port,
            'frame': self.frame,
            'applic': self.applic,
            'server_version': self.serverVersion,
        }