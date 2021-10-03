from api import api
from flask_restx import fields

user_update = api.model("User Update",{
    "sexo": fields.String(max_length=1),
    "nascimento": fields.String,
    "cor": fields.String,
    "telefone": fields.String,
    "rua": fields.String,
    "numero_casa": fields.Integer
})

