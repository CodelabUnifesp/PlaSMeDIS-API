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

user_email = api.model("User E-mail", {
    "user_name": fields.String(),
    "email": fields.String()
})

user_email_list = api.model("Users E-mail List", {
    "count": fields.Integer(),
    "users": fields.List(fields.Nested(user_email))
})

user_create = api.model("User Create",
{
    "real_name": fields.String("realname"),
    "password": fields.String("password"),
    "user_name": fields.String("username"),
    "user_type": fields.Integer(3),
    "bairro": fields.Integer(1),
    "email": fields.String("user@user.com", required=True)
})

user_create_message = api.model("User Create Message", {
    "message": fields.String(),
    "user": fields.Integer()
})