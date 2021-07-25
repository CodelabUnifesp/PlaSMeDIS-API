from flask import request
from api import db
from api.model.notifications import Notificacoes_Conf

def HandleUserNotification(id):
    user_not = Notificacoes_Conf.query.filter_by(usuario=id).first()

    if request.method == 'GET':
        response = {
            "sistema":user_not.sistema,
            "selo_postagem":user_not.selo_postagem,
            "comentario_postagem":user_not.comentario_postagem,
            "saude":user_not.saude,
            "lazer":user_not.lazer,
            "trocas":user_not.trocas
        }
        return {"message": "success", "user_not": response}
    elif request.method == 'PUT':
        data = request.get_json()
        user_not.sistema = data['sistema']
        user_not.selo_postagem = data['selo_postagem']
        user_not.comentario_postagem = data['comentario_postagem']
        user_not.saude = data['saude']
        user_not.lazer = data['lazer']
        user_not.trocas = data['trocas']
        db.session.add(user_not)
        db.session.commit()
        return {"message": f"Configurações de notificação atualizadas"}