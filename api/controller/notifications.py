from flask_cors import cross_origin
from api.util.decorators import token_required
from api.services.notifications import HandleUserNotification
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('notifications', __name__, url_prefix='')

#TODO: separar PUT e GET
#TODO: adicionar json_required PUT
@app.route('/users/<id>/notificacoes_conf', methods=['PUT', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def handle_user_notificacao(id):
    return HandleUserNotification(id)