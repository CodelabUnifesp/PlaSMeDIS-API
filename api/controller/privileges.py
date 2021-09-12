from flask_cors import cross_origin
from api.util.decorators import required
from api.service.privileges import GetPrivileges, PostPrivileges
from flask_restx import Resource
from api import api
import api.model.request.privileges as request
import api.model.response.privileges as response
import api.model.response.default as default

privileges = api.namespace('privileges', description="Privileges namespace")

@privileges.route("")
class Privileges(Resource):
     @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
     @required(response=response.privileges_list, token=True)
     def get(self):
        return GetPrivileges()

     @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
     @required(response=default.message, request=request.privileges, token=True)
     def post(self, data):
        return PostPrivileges(data)