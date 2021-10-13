from flask_cors import cross_origin
from api.util.decorators import required
from api.service.auth import *
from api import api
from flask_restx import Resource
import api.model.request.auth as request
import api.model.response.auth as response
import api.model.response.default as default

auth = api.namespace('auth', description="Auth namespace")

@auth.route("/login")
class Login(Resource):
     @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
     @required(response=response.version, token=False)
     def get(self):
        return GetLogin()

     @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
     @required(response=response.login_response, request=request.credentials, token=False)
     def post(self, data):
        return PostLogin(data)


@auth.route("/forgotpassword")
class ForgotPassword(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.forgot_password, token=False)
    def post(self, data):
        return PostEsqueciSenha(data)
