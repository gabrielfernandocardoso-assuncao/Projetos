from usb import db, login_manager
from datetime import datetime

# Classe usada para informar em qual modelo vai utilizar para fazer login do usuario
from flask_login import UserMixin

# recuperando o usuario
@login_manager.user_loader
def load_user(user_id):

    return Usuario.query.get(user_id)

class Usuario(db.Model, UserMixin): # essa tabela vai ter o login
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String, nullable = True)
    sobrenome = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = True, unique = True)
    senha = db.Column(db.String, nullable = True)
    user = db.relationship('Diagnosticos', backref='user', lazy=True)


class Sintomas(db.Model): # estrutura da tabela
    # atributos
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String, nullable = True)
    sintomas = db.Column(db.String, nullable = True)
    data_envio = db.Column(db.DateTime, default = datetime.utcnow()) # utc - now, o utc entende que de qualquer lugar vai ser um horario universal
    status = db.Column(db.String, default="Enviado")
    diagnosticos = db.relationship('Diagnosticos', backref='diagnostico', lazy=True)

class Diagnosticos(db.Model): # criando a tabela que vai se relacionar com a tabela sintomas
    id = db.Column(db.Integer, primary_key = True)
    resposta = db.Column(db.String, nullable = True)
    relatorio = db.Column(db.String, nullable = True, default='default.png')
    data_criacao = db.Column(db.DateTime, default = datetime.utcnow())

    # relacionando table Usuario
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True )

    # relacionando table sintomas
    sintomas_id = db.Column(db.Integer, db.ForeignKey('sintomas.id'), nullable = True )
