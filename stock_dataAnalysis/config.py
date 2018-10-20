import string

from redis import StrictRedis
import random
import base64

class Config:
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    DEBUG = None
    SECRET_KEY = base64.b64encode(ran_str.encode("utf-8").decode("utf-8"))
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/stock'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #配置redis
    # 地址
    HOST = '127.0.0.1'
    PORT = '6379'
    # 配合状态保持的session信息
    SESSION_TYPE = 'redis'
    # 设置签名
    SESSION_USE_STRING = True
    # redis实例
    SESSION_REDIS = StrictRedis(host=HOST, port=PORT)
    # 配置过期时间
    PREMANET_SESSION_LIFETIME = 3600

class Dev(Config):
    DEBUG = True

class Pro(Config):
    DEBUG = False

config = {
    'development': Dev,
    'production': Pro
}

def add_Blue_print(app):
    pass