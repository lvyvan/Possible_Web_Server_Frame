# 测试 SQLAlchemy
import datetime
import uuid

from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean
from sqlalchemy.orm import sessionmaker, relationship

from faker import Faker

Base = declarative_base()

class User(Base):
    __tablename__ = 'tb_users'
 
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(512), nullable=False)
    uuid = Column(String(512), index=True)
    
    check = Column(String(32))

    create_time = Column(DateTime, default= datetime.datetime.now())
    login_time = Column(DateTime, default= datetime.datetime.now())
    login_ip = Column(String(64))
    login_count = Column(Integer, default=0)
    login_key = Column(String(512))

    rights_groups = Column(Integer, default=0)

    identity_type = Column(String(64))

    nickname = Column(String(64))
    phone = Column(String(32))
    email = Column(String(128))
    age = Column(Integer)
    avatar_img = Column(String(256))

    del_flag = Column(Boolean, default=False)
    def_test = Column(Boolean, default=True)
 
if __name__ == '__main__':
    # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    engine = create_engine("mysql+pymysql://root:yqqlm^gsycl@47.102.210.182/blogdb?charset=utf8mb4", echo=True)
    # Base.metadata.create_all(engine)
    
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    # 创建Session对象
    session = DBSession()
    # faker
    f = Faker(locale='zh_CN')
    # 添加
    
    # 创建User对象，构造测试数据
    for i in range(100):  
        new_user = User()
        new_user.username = f.user_name()
        new_user.password = f.sha256()
        new_user.login_ip = f.ipv4()
        new_user.nickname = f.name()
        new_user.phone = f.phone_number()
        new_user.email = f.email()
        new_user.uuid = str(uuid.uuid1())
        session.add(new_user)
    # 提交
    session.commit()
    # 关闭session
    session.close()
'''
# 利用session创建查询，query(对象类).filter(条件).one()/all()
user = session.query(User).filter(User.id=='5').one()
print('type:{0}'.format(type(user)))
print('name:{0}'.format(user.username))
print(user)
# 关闭session
session.close()

# 更新
session = DBSession()
user_result = session.query(User).filter_by(id='1').first()
user_result.name = "jack"
session.commit()
session.close()

# 删除
session = DBSession()
user_willdel = session.query(User).filter_by(id='5').first()
session.delete(user_willdel)
session.commit()
session.close()
'''