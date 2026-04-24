# importando do pacote flask a classe Flask
from flask import Flask

# startando o aplicativo
app = Flask(__name__) # ele vai iniciar o aplicativo com base nesse arquivo.

# caso der erro de url importar a rota
from usb.views import homepage # importar no final para nao gerar erro