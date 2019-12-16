from urllib import parse
import mimetypes

from cryptography.fernet import Fernet

def main():
    '''
    urlp = parse.urlparse(':8080/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=import%20urllib.parse&oq=python%2520url%25E7%25BC%2596%25E7%25A0%2581&rsv_pq=971c15fb00016df3&rsv_t=d4faSdMXhUqjFvXNhmmuo%2BUnU571rnU1R5aId%2BO2%2FdI%2B%2BG667C6LQIgUEm4&rqlang=cn&rsv_enter=1&rsv_n=2&rsv_sug3=1&bs=python%20url编码')
    print(urlp)
    print(type(urlp))
    print(urlp.path)
    print(urlp.query)
    
    print(mimetypes.guess_type('a.txt'))
    print(mimetypes.guess_type('b.png'))
    print('---------------------------------')
    '''
    key = Fernet.generate_key()
    print(key) # key
    f = Fernet(key) 
    token = f.encrypt(b'cbc751d1-bf08-465e-aed2-ea01a5890c53:fffff')
    print(token)

    info = f.decrypt(token)
    print(info)
    # 解密

'''
b'Yh9cJGYoyEc81s2kg7K8RRCHbt6QM4_FiZGdyKFqDcw='
b'gAAAAABcpexWYZFAMCV9vLVO7JOx_u8yX9NSZrYhxqbelySQCmx-nO_JwFgz6eXGNuKCEJ9mTqmUbub_uH6261xxdKYJPHOI_rScMuGWLiUj3AFKVNZTCSAcjfChMuNOEZekeomc42z-'
b'cbc751d1-bf08-465e-aed2-ea01a5890c53:fffff'
'''


if __name__ == "__main__":
    main()