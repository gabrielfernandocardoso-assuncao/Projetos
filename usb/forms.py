# importando a classe do pacote
from flask_wtf import FlaskForm

# importando o tipo de campo e os validators
from wtforms import StringField, EmailField, PasswordField, SubmitField

# importando os validators
from wtforms.validators import DataRequired, Email

# importando as tabelas e o db
from usb import db
from usb.models import Sintomas

# criando a classe do formulario
class SintomasForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()]) # na variavel, passar o tipo de campo, nome da referencia, passar os validators 
    sintomas = StringField('Sintomas', validators=[DataRequired()]) #
    btnsubmit = SubmitField('Enviar') #

    # criando a função de salvar
    def save(self):
        # instanciando os dados na tabela
        sintomas = Sintomas(
            nome = self.nome.data, # o .data serve para pegar o valor da variavel e nao a variavel em si
            sintomas = self.sintomas.data
        )

        # salvando os dados
        db.session.add(sintomas) # adicionando os dados

        # salvando "literalmente"
        db.session.commit()