from api import api
from flask_restx import fields

credentials = api.model("Credentials", {
    "username": fields.String("username", required=True),
    "password": fields.String("password", required=True)
})

forgot_password = api.model("Forgot Password", {
    "username": fields.String("username", required=True),
    "email": fields.String("email", required=True)
})
