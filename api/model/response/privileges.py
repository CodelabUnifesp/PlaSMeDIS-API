from api import api
from flask_restx import fields

privileges = api.model("Privileges", {
    "user_type": fields.String
})

privileges_list = api.model("User Update",{
    "count": fields.Integer,
    "privileges": fields.Nested(privileges),
    "message": fields.String
})
