from flask import request
from api import db
from api.model.forms import Form_Socioeconomico

#TODO: separar POST e GET
#TODO: remover verificação de método
#TODO: remover verificação de json POST
#TODO: padronizar respostas dos endpoints?
def FormSocio(id):
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_form = Form_Socioeconomico(nome_rep_familia=data['nome_rep_familia'], pessoa=data['pessoa'], qtd_pessoas_familia=data['qtd_pessoas_familia'],
            pessoa_amamenta=data['pessoa_amamenta'], qtd_criancas=data['qtd_criancas'], gestante=data['gestante'], qtd_amamentando=data['qtd_amamentando'], qtd_criancas_deficiencia=data['qtd_criancas_deficiencia'], qtd_gestantes=data['qtd_gestantes'])
            db.session.add(new_form)
            db.session.commit()

            return {"message": f"Formulário enviado!"}
        else:
            return {"error": "O envio não foi feita no formato esperado"}
 
    elif request.method == 'GET':
        forms = Form_Socioeconomico.query.filter_by(pessoa=id).all()
        results = []
        for form in forms:
            if form.preenchido:
                results.append({
                    "preenchido": form.preenchido,
                    "nome_rep": form.nome_rep_familia,
                    "qtd_pessoas": form.qtd_pessoas_familia,
                    "qtd_criancas": form.qtd_criancas,
                    "gestante": form.gestante,
                    "qtd_amamentando": form.qtd_amamentando,
                    "qtd_criancas_deficiencia": form.qtd_criancas_deficiencia,
                    "pessoa_amamenta": form.pessoa_amamenta,
                    "qtd_gestantes": form.qtd_gestantes
                })

        return {"count": len(results), "users": results}

#TODO: separar POST e GET
#TODO: remover verificação de método
#TODO: remover verificação de json POST
def FormSocioGetByUser(user_id):
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            form = Form_Socioeconomico.query.filter_by(pessoa=user_id).first()
            if form is None:
                new_form = Form_Socioeconomico(nome_rep_familia=data['nome_rep_familia'], pessoa=user_id, qtd_pessoas_familia=data['qtd_pessoas_familia'],
                pessoa_amamenta=data['pessoa_amamenta'], qtd_criancas=data['qtd_criancas'], gestante=data['gestante'], qtd_amamentando=data['qtd_amamentando'], qtd_criancas_deficiencia=data['qtd_criancas_deficiencia'], qtd_gestantes=data['qtd_gestantes'])
                db.session.add(new_form)
                db.session.commit()
                return {"status":"1000", "message":"created"}

            else:
                form.nome_rep_familia = data['nome_rep_familia']
                form.qtd_pessoas_familia = data['qtd_pessoas_familia']
                form.pessoa_amamenta = data['pessoa_amamenta']
                form.qtd_criancas = data['qtd_criancas']
                form.gestante = data['gestante']
                form.qtd_amamentando = data['qtd_amamentando']
                form.qtd_criancas_deficiencia = data['qtd_criancas_deficiencia']
                form.qtd_gestantes = data['qtd_gestantes']

                db.session.add(form)
                db.session.commit()

                return {"status":"1000", "message":"updated"}
        else:
            return {"error": "O envio não foi feita no formato esperado"}
    
    elif request.method == 'GET':
        form = Form_Socioeconomico.query.filter_by(pessoa=user_id).one()
        response = {
                "nome_rep_familia": form.nome_rep_familia,
                "qtd_pessoas_familia": form.qtd_pessoas_familia,
                "qtd_criancas": form.qtd_criancas,
                "pessoa_amamenta": form.pessoa_amamenta,
                "qtd_criancas": form.qtd_criancas,
                "gestante": form.gestante,
                "qtd_amamentando": form.qtd_amamentando,
                "qtd_criancas_deficiencia": form.qtd_criancas_deficiencia,
                "qtd_gestantes": form.qtd_gestantes,
        }

        return {"message": "success", "form": response}