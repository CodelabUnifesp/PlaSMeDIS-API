from api import api
from flask_restx import fields

neighborhood = api.model("Bairro",
{
    "id": fields.Integer(),
    "nome": fields.String()
})

neighborhood_list = api.model("Lista de Bairros",
{
    "count": fields.Integer(),
    "Bairros": fields.List(fields.Nested(neighborhood)),
    "message": fields.String()
})