from api import db

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(400), nullable=False)
    criador = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    postagem = db.Column(db.Integer, db.ForeignKey('postagens.id'), nullable=False)
    resposta = db.Column(db.Integer, db.ForeignKey('comentarios.id'), nullable=True)
    data = db.Column(db.Time)

    def __init__(self, texto, criador, postagem, resposta):
        self.texto = texto
        self.criador = criador
        self.postagem = postagem
        self.resposta = resposta
