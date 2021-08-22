from api import api
from flask_restx import fields

user = api.model("User",
{
    "email": fields.String(),
    "privilegio": fields.Integer(),
    "nome": fields.String(),
    "sexo": fields.String(max_length=1),
    "nascimento": fields.String(),
    "cor": fields.String(),
    "telefone": fields.String(),
    "rua": fields.String(),
    "numero_casa": fields.Integer()
})

user_message = api.model("User Message", {
    "message": fields.String(),
    "user": fields.Nested(user)
})