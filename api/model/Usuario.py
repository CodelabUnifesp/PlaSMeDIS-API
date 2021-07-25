from api import flaskApp

db = flaskApp.db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(80), nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    verificado = db.Column(db.Boolean, default=False, nullable=False)
    sexo = db.Column(db.String(1), nullable=True)
    nascimento = db.Column(db.String(20), nullable=True)
    cor = db.Column(db.String(10), nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    rua = db.Column(db.String(100), nullable=True)
    numero_casa = db.Column(db.Integer, nullable=True)
    data_registro = db.Column(db.DateTime, nullable=True)
    bairro = db.Column(db.Integer, db.ForeignKey('bairros.id'), nullable=False)
    user_type = db.Column(db.Integer, db.ForeignKey('privilegios.id'), nullable=False)

    def __init__(self, real_name, password, user_name, user_type, bairro):
        import datetime
        self.real_name = real_name
        self.password = password
        self.verificado = False
        self.user_name = user_name
        self.user_type = user_type
        self.data_registro = datetime.datetime.now()
        self.bairro = bairro

class Privilegio(db.Model):
    __tablename__ = 'privilegios'
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, user_type):
        self.user_type = user_type

class Bairro(db.Model):
    __tablename__ = 'bairros'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome