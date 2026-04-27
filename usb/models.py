from usb import db
from datetime import datetime

class Sintomas(db.Model): # estrutura da tabela
    # atributos
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String, nullable = True)
    sintomas = db.Column(db.String, nullable = True)
    data_envio = db.Column(db.DateTime, default = datetime.utcnow()) # utc - now, o utc entende que de qualquer lugar vai ser um horario universal
    status = db.Column(db.String, default="Enviado")
