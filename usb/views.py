# importando o aplicativo, db (banco)
from usb import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request, redirect

# importando a classe da tabela onde vou salvar
from usb.models import Sintomas

# importando as classes de formulario
from usb.forms import SintomasForm
# passando uma rota
@app.route('/') # rotas sao passadas entre "/"
def homepage(): # função de renderização 

    return render_template('index.html') # renderizando uma string, renderizando um template

# criando a rota para o menu, apos o login
@app.route('/menu/', methods={'GET', 'POST'})
def menu():
    # passando o formulario
    form = SintomasForm() # instanciando o formulario

    if form.validate_on_submit(): # tipo de validação para method post
        form.save() # melhorei o tratamento do formulario

        return redirect( url_for('menu') )
        
    return render_template('menu.html', form=form)

# criando a rota diagnosticos
@app.route('/consultas/')
def consultas():
    context = {}
    # verificando se a requisão é do tipo get, que por padrao é.
    if request.method == 'GET':
        busca = request.args.get('busca', None ) # aqui eu pego o que tá na barra de busca e devolvo como variavel
        context.update({'busca' : busca}) # atualizando o dicionario

    return render_template('consultas.html', context=context)