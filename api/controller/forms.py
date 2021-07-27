from flask_cors import cross_origin
from api.util.decorators import token_required
from api.service.forms import FormSocio, FormSocioGetByUser
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('forms', __name__, url_prefix='')

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/form_socio/<id>', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def form_socio(id):
    return FormSocio(id)

#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/form_socio_by_user_id/<user_id>', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def form_socio_get_by_user(user_id):
    return FormSocioGetByUser(user_id)