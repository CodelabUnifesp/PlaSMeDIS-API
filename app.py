import os
from flask_cors import cross_origin
from api import app
from api.util.decorators import token_required
from api.services.auth import EsqueciSenha, Login
from api.services.forms import FormSocio
from api.services.notifications import HandleUserNotification
from api.services.comments import Comentarios, ComentariosPostagem
from api.services.posts import Filtros, Categorias, ListaPostagens, Postagens, PostagensId, Recomendados, Selo
from api.controller.users import app as users_bp

app.register_blueprint(users_bp)

@app.route('/')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello():
	return "This API Works! [" + os.environ.get("ENV", "DEV") + "]"

@app.route('/users/<id>/notificacoes_conf', methods=['PUT', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def handle_user_notificacao(id):
    return HandleUserNotification(id)

@app.route('/form_socio/<id>', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def form_socio(id):
    return FormSocio(id)

@app.route('/login', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def login():
    return Login()

@app.route('/categorias', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def categorias():
    return Categorias()

@app.route('/selo/<id>', methods=['PUT'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def selo(id):
    return Selo(id)

@app.route('/postagens', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def postagens():
    return Postagens()

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

@app.route('/lista_postagens/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def lista_postagens(id):
    return ListaPostagens(id)

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


@app.route('/esqueci_senha', methods=['Get', 'Post'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def esqueci_senha():
    return EsqueciSenha()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)