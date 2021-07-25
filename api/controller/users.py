from flask_cors import cross_origin
from api.util.decorators import token_required
from api.services.users import Users, Privileges, Bairro, HandleUser, VerifyUsername
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('users', __name__, url_prefix='')

@app.route('/users', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def users():
    return Users()
#TODO: criar controller para privilegios?
@app.route('/privileges', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def privileges():
    return Privileges()
#TODO: criar controller para bairros?
@app.route('/bairros', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def bairros():
    return Bairro()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def handle_user(id):
    return HandleUser(id)

@app.route('/users/username/verify/<username>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def verify_username(username):
    return VerifyUsername(username)