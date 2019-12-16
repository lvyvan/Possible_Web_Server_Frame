from enum import Enum, unique

class X_Frame_Options(Enum):
    '''
    X-Frame-Options : 
        1. DENY 表示该页面不允许在 frame 中展示，即便是在相同域名的页面中嵌套也不允许
        2. SAMEORIGIN 表示该页面可以在相同域名页面的 frame 中展示
        3. ALLOW-FROM uri 表示该页面(uri)可以在指定来源的 frame 中展示
    '''
    DENY = 'DENY'
    SAMEORIGIN = 'SAMEORIGIN'
    ALLOW_FROM_uri = 'ALLOW-FROM'

class Cache_Control(Enum):
    ''' 
    Cache_Control  通用消息头字段被用于在http 请求和响应中通过指定指令来实现缓存机制
        Cache-Control: max-age=<seconds>  -- default 120
        Cache-Control: max-stale[=<seconds>]
        Cache-Control: min-fresh=<seconds>
        Cache-control: no-cache 
        Cache-control: no-store
        Cache-control: no-transform
        Cache-control: only-if-cached
        具体语法详见 https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
    '''
    MAX_AGE_120 = 'max-age=120'
    MAX_STALE = 'max-stale'
    MIN_FRESH_5 = 'min-fresh=5'
    NO_CACHE = 'no-cache'
    NO_STORE = 'no-store'
    NO_TRANSFORM = 'no-transform'
    ONLY_IF_CACHED = 'only-if-cached'

class Connection(Enum):
    '''
    Connection : (决定当前的事务完成后，是否会关闭网络连接)
        1. keep-alive 网络连接就是持久的，不会关闭，使得对同一个服务器的请求可以继续在该连接上完成
        2. close 表明客户端或服务器想要关闭该网络连接，这是HTTP/1.0请求的默认值
    '''
    KEEP_ALIVE = 'keep-alive'
    CLOSE = 'close'

class Encoding(Enum):
    '''
    支持编码，主要是对编码进行限制
        uft-8, gb2312, gbk, gb18030
    '''
    UTF_8 = 'utf-8'
    GB2312 = 'gb2312'
    GBK = 'gbk'
    gb18030 = 'GB18030'



