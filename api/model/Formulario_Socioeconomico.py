from api import db

class Form_Socioeconomico(db.Model):
    __tablename__ = 'form_socioeconomico'
    id = db.Column(db.Integer, primary_key=True)
    nome_rep_familia = db.Column(db.String(100), nullable=False)
    pessoa = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    qtd_pessoas_familia = db.Column(db.Integer, nullable=False)
    qtd_criancas = db.Column(db.Integer, nullable=False)
    gestante = db.Column(db.Boolean, nullable=False)
    qtd_amamentando = db.Column(db.Integer, nullable=False)
    qtd_criancas_deficiencia = db.Column(db.Integer, nullable=False)
    preenchido = db.Column(db.Boolean, nullable=False, default="False")
    pessoa_amamenta = db.Column(db.Boolean, nullable=False, default="False")
    qtd_gestantes = db.Column(db.Integer, nullable=False)
    def __init__(self, nome_rep_familia, pessoa, qtd_pessoas_familia, qtd_criancas, gestante, qtd_amamentando, qtd_criancas_deficiencia, qtd_gestantes, pessoa_amamenta):
        self.nome_rep_familia = nome_rep_familia
        self.pessoa = pessoa
        self.qtd_pessoas_familia = qtd_pessoas_familia
        self.qtd_criancas = qtd_criancas
        self.gestante = gestante
        self.qtd_amamentando = qtd_amamentando
        self.qtd_criancas_deficiencia = qtd_criancas_deficiencia
        self.qtd_gestantes = qtd_gestantes
        self.pessoa_amamenta = pessoa_amamenta
        self.preenchido = True