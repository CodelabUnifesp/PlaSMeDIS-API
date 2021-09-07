from flask_cors import cross_origin
from api.util.decorators import required, token_required
from api.service.users import GetUsers, PostUsers, Privileges, Bairro, VerifyUsername, GetUserId, PutUserId, DelUserId
from flask import Blueprint
from api import api
from flask_restx import Resource
import api.model.request.users as request
import api.model.response.users as response
import api.model.response.default as default

#TODO: adicionar prefixo para as chamadas
app = Blueprint('users', __name__, url_prefix='')

users = api.namespace('users', description="Users namespace")

@users.route("")
class User(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.user_email_list, token=True)
    def get(self):
        return GetUsers()
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.user_create_message, request=response.user_create, token=True)
    def post(self, data):
        return PostUsers(data)

#TODO: criar controller para privilegios?
#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/privileges', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def privileges():
    return Privileges()

#TODO: criar controller para bairros?
#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/bairros', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def bairros():
    return Bairro()

@users.route('/<int:id>')
class UserId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.user_message, token=True)
    def get(self, id):
        return GetUserId(id)

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.user_update, token=True)
    def put(self, data, id):
        return PutUserId(data, id)

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def delete(self, id):
        return DelUserId(id)

@app.route('/users/username/verify/<username>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def verify_username(username):
    return VerifyUsername(username)