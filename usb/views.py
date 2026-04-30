# importando o aplicativo, db (banco)
from usb import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request, redirect, flash

# importando as dependencias de login
from flask_login import login_user, logout_user, current_user, login_required

# importando a classe da tabela onde vou salvar
from usb.models import Sintomas, Diagnosticos

# importando as classes de formulario
from usb.forms import SintomasForm, UserForm, LoginForm, DiagnosticoForm

# passando uma rota
@app.route('/cadastro/', methods=['GET', 'POST']) # rotas sao passadas entre "/"
def homepage(): # função de renderização 
    form = UserForm()
    login_form = LoginForm()

    # verificando login
    if login_form.validate_on_submit():
        user = login_form.login()
        if user:
            login_user(user, remember=True)
            return redirect(url_for('menu'))
        else:
            flash('E-mail ou senha incorretos!', "danger")
    
   # verificando cadastro
    if form.validate_on_submit():
        # Se chegou aqui, o WTForms já validou que o e-mail não é repetido
        user = form.save() 
        if user:
            login_user(user, remember=True)
            return redirect(url_for('menu'))
        else:
            flash("Erro ao criar usuário. Tente novamente.", "danger")

    return render_template('cadastro.html', form=form, login_form=login_form) # renderizando uma string, renderizando um template

# criando a rota de logout
@app.route('/sair/')
@login_required
def Logout():
    logout_user()

    return redirect(url_for('homepage'))


# criando a rota para o menu, apos o login
@app.route('/menu/', methods=['GET', 'POST'])
@login_required
def menu():
    # passando o formulario
    form = SintomasForm() # instanciando o formulario

    if form.validate_on_submit(): # tipo de validação para method post
        form.save() # melhorei o tratamento do formulario

        return redirect( url_for('menu') )
        
    return render_template('menu.html', form=form)

# criando a rota de diagnosticos
@app.route('/diagnosticos/')
@login_required
def diagnosticos():
    # recuperando os diagnosticos
    diagnosticos = Diagnosticos.query.all()

    return render_template('diagnosticos.html', diagnosticos=diagnosticos)
@app.route('/consulta/lista', methods=['GET', 'POST'])
def ConsultaLista():
    busca = ""
    if request.method == 'GET':
        busca = request.args.get('busca', "") # retirando o dado de busca
    
    # variavel de busca
    dados = Sintomas.query.order_by('data_envio') # para orderby para ordenar com base em uma coluna

    if busca != "": # vendo se é diferente de vazio
        dados = dados.filter_by(nome = busca) # filtrando a pesquisa
    context = { 'dados' : dados.all() } # retornando os valores pesquisados do banco
    
    # formulario da resposta do diagnostico
    form = DiagnosticoForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('ConsultaLista'))
    return render_template('consultas.html', context=context, form=form)

# criando a rota status
@app.route('/status/')
@login_required
def Status():
    if request.method == 'GET':
        busca = request.args.get('busca', "")

    dados = Sintomas.query.order_by('data_envio')

    if busca != "":
        dados = dados.filter_by(nome = busca)

    context = { 'dados' : dados.all() }

    return render_template('status.html', context = context)
