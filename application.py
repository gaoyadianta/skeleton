import os
import importlib
from flask import Flask
from config.logger import config_logger
from config import config
from flask_sqlalchemy import SQLAlchemy
import pymysql

db = SQLAlchemy(None, session_options={"expire_on_commit": False})

def register_logger():
    log_level = os.environ.get('LOG_LEVEL') or 'INFO'
    log_file = os.environ.get('LOG_FILE') or 'app.log'
    config_logger(
        enable_console_handler=True,
        enable_file_handler=True,
        log_level=log_level,
        log_file=log_file
    )


def register_app(app):
    for a in config.registered_app:
        module = importlib.import_module(a)
        if hasattr(module, 'register'):
            getattr(module, 'register')(app)


def get_config_object(env=None):
    if not env:
        env = os.environ.get('FLASK_ENV')
    else:
        os.environ['FLASK_ENV'] = env
    if env in config.config_map:
        return config.config_map[env]
    else:
        # set default env if not set
        env = 'production'
        return config.config_map[env]


def create_app_by_config(conf=None):
    # initialize logger
    register_logger()
    # check instance path
    instance_path = os.environ.get('INSTANCE_PATH') or None
    # create and configure the app
    app = Flask(__name__, instance_path=instance_path)
    if not conf:
        conf = get_config_object()
    app.config.from_object(conf)
    init_database(app)
    # ensure the instance folder exists
    if app.instance_path:
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass
    # register app
    register_app(app)
    return app

def init_database(app):
    pymysql.install_as_MySQLdb()
    DATA_BASE_PATH = 'mysql://root:chuangxin@127.0.0.1:3306/jms_backend'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_PATH
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 100
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 100
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 1200

    db.init_app(app=app)
    with app.app_context():
        db.create_all()

def create_app(env=None):
    conf = get_config_object(env)
    return create_app_by_config(conf)
