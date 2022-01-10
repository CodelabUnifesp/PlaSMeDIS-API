from api import db
from api.model.database.users import Usuario
from api.model.database.notifications import Notificacoes_Conf

def UserToDict(user: Usuario):
    return {
        "id": user.id,
        "real_name": user.real_name,
        "verificado": user.verificado,
        "user_name": user.user_name,
        "user_type": user.user_type,
        "email": user.email
    }

#TODO: padronizar respostas dos endpoints?
def PostUsers(data):
    new_user = Usuario(real_name=data['real_name'], password=data['password'], user_name=data['user_name'], user_type=data['user_type'], bairro=data['bairro'])
    if "email" in data:
        new_user.email = data['email']
    db.session.add(new_user)
    db.session.commit()
    
    new_user = Usuario.query.filter_by(user_name=data['user_name'],real_name=data['real_name']).first()
    new_user_not = Notificacoes_Conf(usuario=new_user.id, sistema=False, selo_postagem=False, comentario_postagem=False, saude=False, lazer=False, trocas=False)
    db.session.add(new_user_not)
    db.session.commit()

    return {"message": f"Usuario criado", "user": new_user.id}

def GetUsers():
    users = Usuario.query.all()
    results = [
        {
            "user_name": user.user_name,
            "email": user.email
        } for user in users]

    return {"count": len(results), "users": results, "message": "success"}

def GetUserId(id):
    user = Usuario.query.get_or_404(id)
    response = {
        "email": user.email,
        "privilegio": user.user_type,
        "nome": user.real_name,
        "sexo": user.sexo,
        "nascimento": user.nascimento,
        "cor": user.cor,
        "telefone": user.telefone,
        "rua": user.rua,
        "numero_casa": user.numero_casa
    }
    return {"message": "success", "user": response}

#TODO: fazer alguns campos serem opcionais?
def PutUserId(data, id):
    user = Usuario.query.get_or_404(id)
    #user.email = data['email']
    #user.real_name = data['real_name']
    #user.password = data['password']
    user.verificado = True
    user.sexo = data['sexo']
    user.nascimento = data['nascimento']
    user.cor = data['cor']
    user.telefone = data['telefone']
    user.rua = data['rua']
    user.numero_casa = data['numero_casa']

    db.session.add(user)
    db.session.commit()

    return {"message": f"Dados de {user.user_name} atualizados"}

def DelUserId(id):
    user = Usuario.query.get_or_404(id)
    notificacoes = Notificacoes_Conf.query.filter_by(usuario=id).first()
    if notificacoes:
        db.session.delete(notificacoes)
    db.session.delete(user)
    db.session.commit()

    return {"message": f"Dados de {user.user_name} removidos"}

def GetVerify(username):
    user = Usuario.query.filter_by(user_name=username).first()
    if user:
        return { "success": False, "message": "User with username '" + str(username) + "' already exists." }
    else:
        return { "success": True, "message": "Username '" + str(username) + "' is available."}