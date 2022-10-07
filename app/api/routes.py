from app.api.resources.EventList import Eventlist
from flask import Blueprint
from flask_restful import Api


back = Blueprint('api', __name__)

api = Api(back)

api.add_resource(Eventlist, '/')
