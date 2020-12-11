from flask import Blueprint
from flask_restful import Api
from app.api.health import *
from app.api.sms import Sms


api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

api.add_resource(Health, '/health')
api.add_resource(Test, '/test')
api.add_resource(Sms, '/sms')
