from flask import request
from api import db
from api.model.database.users import Bairro

def PostNeighborhoods(data):
    new_bairro = Bairro(nome=data['nome'])

    db.session.add(new_bairro)
    db.session.commit()

    return {"message": f"Bairro criado com sucesso"}
    
def GetNeighborhoods():
    bairros = Bairro.query.all()
    results = [
        {
            "nome": bairro.nome,
            "id": bairro.id
        } for bairro in bairros]

    return {"count": len(results), "Bairros": results, "message": "success"}