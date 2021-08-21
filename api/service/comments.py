from flask import request
from api import db
from api.model.database.comments import Comentario
from api.model.database.users import Usuario

#TODO: separar POST e GET
#TODO: remover verificação de método
#TODO: remover verificação de json POST
#TODO: padronizar respostas dos endpoints?
def Comentarios():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_comment = Comentario(texto=data['texto'], criador=data['criador'], resposta=data['resposta'], postagem=data["postagem"])

            db.session.add(new_comment)
            db.session.commit()

            return {"message": f"Comentário registrado"}
        else:
            return {"error": "A requisição não está no formato esperado"}

    elif request.method == 'GET':
        comments = Comentario.query.all()
        results = [
            {
                "texto": comment.texto,
                "criador": comment.criador,
                "postagem": comment.postagem,
                "resposta": comment.resposta,
                "data": comment.data
            } for comment in comments]

        return {"count": len(results), "comments": results, "message": "success"}

#TODO: remover verificação de método
def ComentariosPostagem(postagem_id):
    if request.method == 'GET':
        comments = Comentario.query.filter_by(postagem=postagem_id).all()
        users_id = [ comment.criador for comment in comments ]
        users = Usuario.query.filter(Usuario.id.in_(users_id)).all()
        results = [
        {
            "texto": comment.texto,
            "criador":
                {
                    "id": comment.criador,
                    "name": next(filter(lambda user: user.id == comment.criador, users)).real_name
                },
            "resposta": comment.resposta,
            "data": comment.data
        } for comment in comments]
        return {"user": 1,"count": len(results), "comments": results, "message": "success"}