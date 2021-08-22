from flask_cors import cross_origin
from api.util.decorators import required, token_required
from api.service.users import Users, Privileges, Bairro, VerifyUsername, GetUserId, PutUserId, DelUserId
from flask import Blueprint
from api import api
from flask_restx import Resource
import api.model.request.users as request
import api.model.response.users as response
import api.model.response.default as default

#TODO: adicionar prefixo para as chamadas
app = Blueprint('users', __name__, url_prefix='')

users = api.namespace('users', description="Users namespace")

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/users', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def userss():
    return Users()

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