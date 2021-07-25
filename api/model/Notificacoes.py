from api import db

class Notificacoes_Conf(db.Model):
    __tablename__ = 'notificacoes_conf'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    sistema = db.Column(db.Boolean, default=False, nullable=False)
    selo_postagem = db.Column(db.Boolean, default=False, nullable=False)
    comentario_postagem = db.Column(db.Boolean, default=False, nullable=False)
    saude =db.Column(db.Boolean, default=False, nullable=False)
    lazer = db.Column(db.Boolean, default=False, nullable=False)
    trocas = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, usuario, sistema, selo_postagem, comentario_postagem, saude, lazer, trocas):
        self.usuario = usuario
        self.sistema = sistema
        self.selo_postagem = selo_postagem
        self.comentario_postagem = comentario_postagem
        self.saude = saude
        self.lazer = lazer
        self.trocas = trocas