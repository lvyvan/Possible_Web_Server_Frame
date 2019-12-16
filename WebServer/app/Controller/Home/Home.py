#_*_ coding:utf-8 _*_
import re
import hashlib
import datetime
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from app.Templates.Template import Template
from app.apps.view import View
from app.Model.model import User
from app.Tools.verificationCode import verify_code

class Home(View):
    def __init__(self, context):
        super().__init__(context)
        super().AddRoutDic({
            # 注册控制器
                "^index$": self.index,
                "^login$": self.login,
                "^login_check": self.login_check,
                "^getverification_code$": self.getverification_code
            })
        # 注册模板
        self.templates = Template("/home")
        self.engine = create_engine("mysql+pymysql://root:yqqlm^gsycl@47.102.210.182/blogdb?charset=utf8mb4", echo=True)
        # 创建DBSession类型
        self.DBSession = sessionmaker(bind=self.engine)

    def index(self, context, result):
        username = context.Request.Cookie.GetCookie("username")
        check = context.Request.Cookie.GetCookie("check")
        if (username != None and check != None):
            dbsession = self.DBSession()
            user = dbsession.query(User).filter(User.username==username).first()
            if(check == hashlib.sha256(user.uuid.encode('utf-8')).hexdigest()):
                context.Request.Session.Set('user_id', user.id)
                client_address_ip, port = context.Request.SERVER_NAME
                user.login_ip = client_address_ip
                user.login_count += 1
                user.login_time = datetime.datetime.now()
                user_info = '<p>username: %s</p>' %user.username
                user_info += '<p>nickname: %s</p>' %user.nickname
                user_info += '<p>phone: %s</p>' %user.phone
                user_info += '<p>email: %s</p>' %user.email
                userinfos = {
                    'status': '已经自动登陆',
                    'user_info': user_info,
                }
            else:
                userinfos = {'status': '未登陆，请先登录','user_info': ''}
            dbsession.close()
        else:
            userinfos = {'status': '未登录，请先登录','user_info': ''}
        # 此处尚需处理 登陆事宜
        content = self.templates.retContent('/index.html', userinfos)
        context.Response.Set_Content_Type('a.html')
        return content

    def login(self, context, result):
        content = self.templates.retContent('/login.html', {})
        context.Response.Set_Content_Type('a.html')
        return content

    def getverification_code(self, context, result):
        code, img = verify_code()
        context.Request.Session.Set('verification_code', code)
        context.Response.Set_Content_Type('a.png')
        return img

    def login_check(self, context, result):
        checkvalue = context.Request.Possible_request_parameter['checkvalue']
        verification_code = context.Request.Session.Get4deCode('verification_code')
        if 1:#checkvalue.upper() == verification_code.upper():
            username = context.Request.Possible_request_parameter['username']
            password = context.Request.Possible_request_parameter['password']
            automatic_login = context.Request.Possible_request_parameter['automatic_login']

            dbsession = self.DBSession()
            user = dbsession.query(User).filter(User.username==username).first()
            if user != None:
                passwordkey = (password + user.uuid).encode('utf-8')
                key = hashlib.sha256(passwordkey)
                if user.password == key.hexdigest():
                    # 已成功 mlai - 123
                    content = '1'
                    context.Request.Session.Set('user_id', user.id)
                    client_address_ip, port = context.Request.SERVER_NAME
                    user.login_ip = client_address_ip
                    user.login_count += 1
                    user.login_time = datetime.datetime.now()
                    if automatic_login == 'ok':
                        ciphertext = hashlib.sha256(user.uuid.encode('utf-8')).hexdigest()
                        # cookie 注册
                        context.Request.Cookie.sCookie["username"] = user.username
                        context.Request.Cookie.sCookie["username"]["path"] = "/"
                        context.Request.Cookie.sCookie["username"]['max-age'] = 604800
                        # cookie 校验码注册
                        context.Request.Cookie.sCookie["check"] = ciphertext
                        context.Request.Cookie.sCookie["check"]["path"] = "/"
                        context.Request.Cookie.sCookie["check"]['max-age'] = 604800
                    dbsession.add(user)
                    # 提交
                    dbsession.commit()
                    dbsession.close()
                else:
                    content = '0'
            else:
                content = '0'
        else:
            content = '-1'
        context.Response.Set_Content_Type('a.txt')
        return content

    def create_user(self, context, result):
        pass