from api import api
from flask_restx import fields

privileges = api.model("Privileges", {
    "user_type": fields.String
})