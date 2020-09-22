import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig:
    SECRET_KEY = 'secret string'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # # 关闭追踪数据库的修改
    WTF_I18N_ENABLED = False
    MAX_CONTENT_LENGTH = 3*1024*1024

class DevelomentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

config = {
    'development': DevelomentConfig,
    'production': ProductionConfig
}