from flask_restful import Resource
import logging
from config.logger import logger
import json
from application import db
from app.model import Device

class Health(Resource):

    def get(self):
        logger.error('here')
        return {'message': 'ok'}, 200

class Test(Resource):

    def get(self):
        ret = db.session.query(Device).first()
        
        logger.error('test')
        return {'message':ret.name, 'status':0}
