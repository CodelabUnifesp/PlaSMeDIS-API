from flask_cors import cross_origin
from api.util.decorators import required
from api.service.neighborhoods import GetNeighborhoods, PostNeighborhoods
from api import api
from flask_restx import Resource
import api.model.request.users as request
import api.model.response.users as response
import api.model.response.default as default

neighborhoods = api.namespace('neighborhoods', description="Neighborhood namespace")

@neighborhoods.route("")
class User(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self):
        return GetNeighborhoods()
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.user_create_message, token=False)
    def post(self, data):
        return PostNeighborhoods(data)