# 测试 SQLAlchemy
import datetime
import uuid

from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'tb_users'
 
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(512), nullable=False)
    uuid = Column(String(512), default=str(uuid.uuid1()), index=True)
    
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
    Base.metadata.create_all(engine)
