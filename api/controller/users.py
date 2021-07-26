from flask_cors import cross_origin
from api.util.decorators import json_required, token_required
from api.service.users import Users, Privileges, Bairro, VerifyUsername, GetUserId, PutUserId, DelUserId
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('users', __name__, url_prefix='')

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/users', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def users():
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

@app.route('/users/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def get_user_id(id):
    return GetUserId(id)

@app.route('/users/<id>', methods=['PUT'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
@json_required
def put_user_id(data, id):
    return PutUserId(data, id)

@app.route('/users/<id>', methods=['DELETE'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def del_user_id(id):
    return DelUserId(id)

@app.route('/users/username/verify/<username>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def verify_username(username):
    return VerifyUsername(username)