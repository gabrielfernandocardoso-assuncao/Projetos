# importando o aplicativo, db (banco)
from usb import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request, redirect, flash

# importando as dependencias de login
from flask_login import login_user, logout_user, current_user

# importando a classe da tabela onde vou salvar
from usb.models import Sintomas

# importando as classes de formulario
from usb.forms import SintomasForm, UserForm
# passando uma rota
@app.route('/cadastro/', methods=['GET', 'POST']) # rotas sao passadas entre "/"
def homepage(): # função de renderização 
    form = UserForm()
    if form.validate_on_submit():
        # Se chegou aqui, o WTForms já validou que o e-mail não é repetido
        user = form.save() 
        if user:
            login_user(user, remember=True)
            return redirect(url_for('menu'))
        else:
            flash("Erro ao criar usuário. Tente novamente.", "danger")
    return render_template('cadastro.html', form=form) # renderizando uma string, renderizando um template

# criando a rota para o menu, apos o login
@app.route('/menu/', methods=['GET', 'POST'])
def menu():
    # passando o formulario
    form = SintomasForm() # instanciando o formulario

    if form.validate_on_submit(): # tipo de validação para method post
        form.save() # melhorei o tratamento do formulario

        return redirect( url_for('menu') )
        
    return render_template('menu.html', form=form)

# criando a rota diagnosticos
@app.route('/consulta/lista')
def ConsultaLista():
    if request.method == 'GET':
        busca = request.args.get('busca', "") # retirando o dado de busca
    
    # variavel de busca
    dados = Sintomas.query.order_by('data_envio') # para orderby para ordenar com base em uma coluna

    if busca != "": # vendo se é diferente de vazio
        dados = dados.filter_by(nome = busca) # filtrando a pesquisa
    context = { 'dados' : dados.all() } # retornando os valores pesquisados do banco
    
    return render_template('consultas.html', context=context)

# criando a rota status
@app.route('/status/')
def Status():
    if request.method == 'GET':
        busca = request.args.get('busca', "")

    dados = Sintomas.query.order_by('data_envio')

    if busca != "":
        dados = dados.filter_by(nome = busca)

    context = { 'dados' : dados.all() }

    return render_template('status.html', context = context)
