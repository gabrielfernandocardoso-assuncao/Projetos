# importando do pacote flask a classe Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# importando a biblioteca os
import os # serve de interação, é necessario

# carregando a biblioteca de ambiente virtual
from dotenv import load_dotenv

# carregando o arquivo
load_dotenv('.env') # esse arquivo pode ter qualquer nome

# startando o aplicativo
app = Flask(__name__) # ele vai iniciar o aplicativo com base nesse arquivo.

# definindo o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') # acessando variavel do ambiente virtual

# verificador do banco de dados 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# token de segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # acessando as variaveis do ambiente virtual

# definindo a variavel do banco de dados
db = SQLAlchemy(app)

# definindo o app de migrate
migrate = Migrate(app, db)

# caso der erro de url importar a rota
from usb.views import homepage # importar no final para nao gerar erro

# importanto a tabela 
from usb.models import Sintomas
