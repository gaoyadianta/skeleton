from flask import Blueprint
from flask_restful import Api
from name.api.first import First

name_bp = Blueprint('name', __name__, url_prefix='/name')
api = Api(name_bp)

api.add_resource(First, '/first')
