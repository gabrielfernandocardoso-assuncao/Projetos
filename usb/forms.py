# importando a classe do pacote
from flask_wtf import FlaskForm

# importando o tipo de campo e os validators
from wtforms import StringField, EmailField, PasswordField, SubmitField, PasswordField

# importando os campos de arquivo
from flask_wtf.file import FileField, FileAllowed

# importando os validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

# importando as tabelas e o db
from usb import db, bcrypt, app
from usb.models import Sintomas, Usuario, Diagnosticos

# biblioteca usada pra salvar arquivo 
import os

# segurança no bd
from werkzeug.utils import secure_filename

# criando o formulario de Login
class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    # função validator
    def validate_email(self, email): # tem que ser 'validate_' e o nome do campo 'email'
        if Usuario.query.filter_by(email=email.data).first(): # first pega o primeiro resultado, data pega o que tem dentro da variavel.
            return ValidationError('Usuario já cadastrado com esse email!!')
        
    # função de salvar
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8')) # encode('utf-8') para aceitar escrita brasileira, boa pratica

        # criando o Usuario
        usuario = Usuario(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        # salvando 
        db.session.add(usuario)
        db.session.commit()

        return usuario

# criando o formulario de login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    # função de login
    def login(self):
        # recuperar o usuario do email
        user = Usuario.query.filter_by(email=self.email.data).first()

        # verificar se a senha é valida
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                # retorna o usuario
                return user 
            else:
                raise Exception("Senha incorreta!!")
        else:
            return None

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

class DiagnosticoForm(FlaskForm):
    resposta = StringField('Diagnostico', validators=[DataRequired()])
    relatorio = FileField('Relatorio/PDF', validators=[ DataRequired(), FileAllowed(['png', 'pdf', 'jpg'])]) # criando o campo
    btnsubmit = SubmitField('Enviar')

    def save(self, sintomas_id):
        relatorio = self.relatorio.data
        nome_seguro = secure_filename(relatorio.filename)
        diagnostico = Diagnosticos (
            resposta = self.resposta.data,
            sintomas_id = sintomas_id,
            relatorio = nome_seguro # salvando na tabela o arquivo
        )

        caminho = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), # vai buscar o caminho configurado pra salvar no init
            # importar o app tambem
            app.config['UPLOAD_FILE'],
            # definir qual pasta vai salvar
            'diagnostico',
            nome_seguro
        )
        
        relatorio.save(caminho)
        db.session.add(diagnostico)
        db.session.commit()