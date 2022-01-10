from api import api
from flask_restx import fields

neighborhood = api.model("Create Neighborhood",
{
    "nome": fields.String()
})