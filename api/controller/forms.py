from flask_cors import cross_origin
from api.util.decorators import token_required
from api.services.forms import FormSocio
from flask import Blueprint

#TODO: adicionar prefixo para as chamadas
app = Blueprint('forms', __name__, url_prefix='')

@app.route('/form_socio/<id>', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def form_socio(id):
    return FormSocio(id)