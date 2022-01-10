from flask_cors import cross_origin
from api.util.decorators import required
from api.service.neighborhoods import GetNeighborhoods, PostNeighborhoods
from api import api
from flask_restx import Resource
import api.model.request.neighborhoods as request
import api.model.response.neighborhoods as response
import api.model.response.default as default

neighborhoods = api.namespace('neighborhoods', description="Neighborhood namespace")

@neighborhoods.route("")
class User(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.neighborhood_list, token=True)
    def get(self):
        return GetNeighborhoods()
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.neighborhood, token=True)
    def post(self, data):
        return PostNeighborhoods(data)