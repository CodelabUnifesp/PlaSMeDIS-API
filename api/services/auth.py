import os
import jwt
import datetime
import smtplib
import random
from flask import request
from api import db, app
from api.model.Usuario import Usuario
from api.services.users import UserToDict
from functools import wraps

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
        token = None
        try:
            token = request.headers['Authorization'].split("Bearer ")[1]
        except:
            return {'message': 'a valid token is missing'}

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], issuer=os.environ.get('ME', 'plasmedis-api-local'), algorithms=["HS256"], options={"require": ["exp", "sub", "iss", "aud"], "verify_aud": False, "verify_iat": False, "verify_nbf": False})
        except jwt.exceptions.InvalidKeyError:
            return {'message': 'Secret Key is not in the proper format'}
        except jwt.exceptions.InvalidAlgorithmError:
            return {'message': 'Algorithm is not recognized by PyJWT'}
        except jwt.exceptions.ExpiredSignatureError:
            return {'message': 'Token is expired'}
        except jwt.exceptions.InvalidIssuerError:
            return {'message': 'Token has a different issuer'}
        except jwt.exceptions.MissingRequiredClaimError:
            return {'message': 'Token is missing a required claim'}
        except jwt.exceptions.DecodeError:
            return {'message': 'Token failed validation'}
        except Exception as ex:
            return {'message': 'There was a error decoding the token'}

        return f(*args, **kwargs)
   return decorator

def Login():
    AUTH_VERSION = os.environ.get("AUTH_VERSION", 0.2)

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            user = Usuario.query.filter_by(user_name=data['username']).first()
            if user is None:
                user = Usuario.query.filter_by(email=data['username']).first()
            if user:
                if user.password == data['password']:
                    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=7)
                    issuedAt = datetime.datetime.utcnow()
                    token = jwt.encode({'auth': AUTH_VERSION, 'exp': expiration, 'iat': issuedAt, 'sub': user.id, 'iss': os.environ.get('ME', 'plasmedis-api-local'), 'aud': request.args.get('aud', 'unknown')}, app.config['SECRET_KEY'], algorithm="HS256")
                    return {"status": 1000, "user": UserToDict(user), "token": token, "verificado": str(user.verificado)} #Valido
                else:
                    return {"status": 1010} #Invalido
            else:
                return {"status": 1010} #Invalido
        else:
            return {"error": "A requisição não foi feita no formato esperado"}
    elif request.method == 'GET':
        # retorna um marcador de versão, para quando as mudanças no token forem tão significativas que o único
        # jeito de atualizar algo no front vai ser matando a sessão atual do usuário
        return {'version': AUTH_VERSION}

def EsqueciSenha():
     if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            usuario = data["id"]
            usuario = int(usuario)
            row = Usuario.query.filter_by(id=usuario).one()

            #Conecta e inicia o serviço de email
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            res = smtpObj.starttls()

            #Criei essa conta para mandar o email
            smtpObj.login('codelabtesteesquecisenha@gmail.com', '44D6DDAAC9C660F72D6490D7CC44731BEA7C236A9241B387D3E9AF0C66B30D49')

            #Gera uma hash que servirá como senha temporaria
            hash = str(random.getrandbits(128))
            email =  row.email
            row.password = hash
            db.session.add(row)
            db.session.commit()
            msg = "\n\nSua nova senha e " +hash
            smtpObj.sendmail('codelabtesteesquecisenha@gmail.com',email,  msg )

            return("A senha temporaria foi enviada para o email " + row.email)

        else:
            return {"error": "A requisição não está no formato esperado"}