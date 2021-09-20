import os
import jwt
import datetime
import smtplib
import random
from flask import request
from api import db, app
from api.model.database.users import Usuario
from api.service.users import UserToDict

#TODO: separar POST e GET
#TODO: remover verificação de método
#TODO: remover verificação de json POST
#TODO: padronizar respostas dos endpoints?
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

#TODO: remover verificação de método
#TODO: remover verificação de json POST
def EsqueciSenha():
     if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get("username", None)
            email = data.get("email", None)

            if username is None or username == '':
                row = Usuario.query.filter_by(email=email).first()
            else:
                row = Usuario.query.filter_by(user_name=username).first()

            # Conecta e inicia o serviço de email
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            res = smtpObj.starttls()

            # Criei essa conta para mandar o email
            smtpObj.login('codelabtesteesquecisenha@gmail.com', '44D6DDAAC9C660F72D6490D7CC44731BEA7C236A9241B387D3E9AF0C66B30D49')

            # Gera uma hash que servirá como senha temporaria
            hash = str(random.getrandbits(128))
            email = row.email
            row.password = hash
            db.session.add(row)
            db.session.commit()
            msg = "\n\nSua nova senha e " +hash
            smtpObj.sendmail('codelabtesteesquecisenha@gmail.com', email, msg)

            return "A senha temporaria foi enviada para o email " + row.email

        else:
            return {"error": "A requisição não está no formato esperado"}