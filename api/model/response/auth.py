from api.util.decorators import required
from api import api
from flask_restx import fields

login_user = api.model("Login User",{
    "id": fields.Integer,
    "real_name": fields.String,
    "verificado": fields.Boolean,
    "user_name": fields.String,
    "user_type": fields.Integer,
    "email": fields.String
})

login_response = api.model("Login Response",{
    "status": fields.Integer,
    "user": fields.Nested(login_user, allow_null=True),
    "token": fields.String(),
    "verificado": fields.String()
})

version = api.model("Version",{
    "version": fields.String
})