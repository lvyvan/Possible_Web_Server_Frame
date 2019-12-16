#_*_ coding:utf-8 _*_
import redis

class Cache(object):
    def __init__(self):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)  
        self.sr = redis.Redis(connection_pool=pool)  

    def Set(self, key, value):
        '''设置 key 值'''
        return self.sr.set(key, value)
         
    def Get(self, key):
        '''获取 key 值'''
        return self.sr.get(key)

    def Get4decode(self, key):
        '''获取 key 值，并decode'''
        return self.sr.get(key).decode()

    def Setnx(self, key, value):
        '''若该 Key 不存在，则进行设置'''

    def GetSet(self, key, value):
        '''获取当前Cache的值，并赋予新值'''
        return self.sr.getset(key, value)

    def Setex(self, key, value, time = 3600):
        '''设置当前 key 的 Value, 并设置有效期，默认 1h '''
        return self.sr.setex(key, time, value)

    def Append(self, key, value):
        '''指定 key 后进行追加 value'''
        return self.sr.append(key, value)

    def Exists(self, key):
        '''查询 Cache 是否存在'''
        return self.sr.exists(key)

    def Delete(self, key):
        '''删除指定的key'''
        return self.sr.delete(key)

    def Rename(self,key, rekey):
        '''Cache重命名'''
        return self.sr.rename(key, rekey)

    def Expire(self, key, time):
        '''设置 Cache的有效期时间 '''
        return self.sr.expire(key, time)

    def Ttl(self, key):
        '''查询有效期'''
        return self.sr.ttl(key)

    def Flushadb(self):
        '''清空当前存在的Cache'''
        return self.sr.flushdb()

def main():
    cache = Cache()
    print(cache.Set('name', 'Yym'))
    print(cache.Get('name'))
    print(cache.Get4decode('name'))
    print(cache.Setnx('age', 18))
    print(cache.GetSet('age', 24))
    print(cache.Setex('gender','0', time=1800))
    print(cache.Append('name', '_'))
    print(cache.Exists('name'))
    print(cache.Delete('age'))
    print(cache.Expire('name', 1888))
    print(cache.Ttl('name'))
    print(cache.Flushadb())

'''
# python3 Cache.py
    True
    b'Yym'
    Yym
    None
    None
    True
    4
    1
    1
    True
    1888
    True
'''


if __name__ == "__main__":
    main()