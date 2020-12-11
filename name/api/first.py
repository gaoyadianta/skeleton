from flask_restful import Resource
import logging

class First(Resource):

    def get(self):
        logging.info('here')
        return {'message': 'ok'}, 200
