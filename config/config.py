import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    DEBUG = False
    TESTING = False

    APP_HOST = '127.0.0.1'
    APP_PORT = 5005


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


registered_app = [
    'app',
    'name'
]

config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
