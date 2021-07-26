from flask_cors import cross_origin
from api.util.decorators import token_required
from api.services.comments import Comentarios, ComentariosPostagem
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('comments', __name__, url_prefix='')

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/comentarios', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def comentarios():
    return Comentarios()

@app.route('/comentarios/<postagem_id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def comentarios_postagem(postagem_id):
    return ComentariosPostagem(postagem_id)