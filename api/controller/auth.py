from flask_cors import cross_origin
from api.util.decorators import token_required
from api.service.auth import Login, EsqueciSenha
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('auth', __name__, url_prefix='')

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/login', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def login():
    return Login()

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/esqueci_senha', methods=['Get', 'Post'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def esqueci_senha():
    return EsqueciSenha()

