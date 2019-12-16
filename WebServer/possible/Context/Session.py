#_*_ coding:utf-8 _*_
import hashlib
import random
import time

import redis


class Session(object):
    def __init__(self, ip):
        self.sr = None
        self.Ip = ip
        self.sessionid = None

    def CreateSession(self, sessionid = None):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)  
        self.sr = redis.Redis(connection_pool=pool)
        if sessionid == None:
            self.Get2Set()
        else:
            self.SetSessionId(sessionid)

    def SetSessionId(self, sessionid):
        '''设置SessionId'''
        self.sessionid = sessionid

    @classmethod
    def GetSessionid(cls, ip):
        '''返回sessionId'''
        data = (str(random.random()) + str(time.time()) + str(ip)).encode("utf-8")
        m = hashlib.sha256()
        m.update(data)
        return m.hexdigest()

    def Get2Set(self):
        '''生成一个SessionId, 并设置'''
        self.sessionid = Session.GetSessionid(self.Ip)
        return self.sessionid

    def Set(self, key, value):
        '''设置/修改 key 值'''
        if self.sr.hset(self.sessionid, key, value):
            return self.Expire('1800')
        return False
         
    def Get(self, key):
        '''获取 key 值'''
        return self.sr.hget(self.sessionid, key)

    def Get4deCode(self, key):
        '''获取 Key 值,并解码'''
        if self.Get(key) == None:
            return None
        else:
            return self.Get(key).decode()

    def Hexists(self, key):
        '''查询 key 是否存在'''
        return self.sr.hexists(self.sessionid, key)

    def HdelSession(self, key):
        '''删除 key 值 '''
        return self.sr.hdel(self.sessionid, key)

    def ExistsSessionid(self):
        '''查询 SessionId 是否存在'''
        return self.sr.exists(self.sessionid)

    def Expire(self, second):
        '''设置Session时间'''
        return self.sr.expire(self.sessionid, second)

    def Ttl(self):
        '''查询时间'''
        return self.sr.ttl(self.sessionid)

    def DelSession(self):
        '''删除当前Session, Sessionid = None'''
        ret = self.sr.delete(self.sessionid)
        self.sessionid = None
        return ret


def main():
    session = Session('127.0.0.1')
    session.CreateSession()
    print(session.Get2Set())                    # 42de7a040d550a5ca70cf9132830925bb40171cad2c1fc5ae9a7f42530ae192f
    print(session.Set('name', 'yangyueming'))   # True
    print(session.Ttl())                        # 1800
    print(session.Expire('3600'))               # True
    print(type(session.Get('name')), session.Get4deCode('name'))   # <class 'bytes'> 'yangyueming'
    print(session.Hexists('name'))              # True
    print(session.HdelSession('name'))          # 1
    print(session.DelSession())                 # 0

if __name__ == "__main__":
    main()
