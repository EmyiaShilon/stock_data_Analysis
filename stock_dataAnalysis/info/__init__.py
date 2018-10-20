from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
import logging
from logging.handlers import RotatingFileHandler
from flask_wtf import CSRFProtect,csrf

from config import Config, config,add_Blue_print

# 实例化数据操作对象
db = SQLAlchemy()
# 实例化redis数据库对象
redis_store = StrictRedis(host=Config.HOST, port=Config.PORT, decode_responses=True)
# 设置日志等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器
file_log_handler = RotatingFileHandler("logs/log",maxBytes=1024*1024*10,backupCount=10)
#设置日志格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为日志记录器设置记录格式
file_log_handler.setFormatter(formatter)
#
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    config.add_Blue_print(app)
    Session(app)
    CSRFProtect(app)
    @app.after_request
    def after_request(response):
        csrf_token = csrf.generate_csrf()
        response.set_cookie('csrf_token',csrf_token)
        return response
    return app
