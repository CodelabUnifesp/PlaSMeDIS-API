from flask_cors import cross_origin
from api.util.decorators import token_required
from api.service.posts import Categorias, Selo, Postagens, Recomendados, Filtros, PostagensId, ListaPostagens
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('posts', __name__, url_prefix='')

#TODO: criar controller para categorias?
#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/categorias', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def categorias():
    return Categorias()

#TODO: adicionar json_required PUT
@app.route('/selo/<id>', methods=['PUT'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def selo(id):
    return Selo(id)

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/postagens', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def postagens():
    return Postagens()

#TODO: criar controller para recomendados?
@app.route('/recomendados', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def recomendados():
    return Recomendados()

@app.route('/postagens/categorias/<id_categoria>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def filtros(id_categoria):
    return Filtros(id_categoria)

@app.route('/postagens/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def postagensId(id):
    return PostagensId(id)

#TODO: padronizar nome?
@app.route('/lista_postagens/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def lista_postagens(id):
    return ListaPostagens(id)