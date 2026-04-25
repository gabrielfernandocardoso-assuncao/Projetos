# importando o aplicativo, db (banco)
from usb import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request

# importando a classe da tabela onde vou salvar
from usb.models import Sintomas

# passando uma rota
@app.route('/') # rotas sao passadas entre "/"
def homepage(): # função de renderização 

    return render_template('index.html') # renderizando uma string, renderizando um template

# criando a rota para o menu, apos o login
@app.route('/menu/', methods={'GET', 'POST'})
def menu():
    if request.method == 'POST':
        nome = request.form['nome'] # recupero o nome em uma variavel
        sintomas = request.form['sintomas'] # recupero o sintomas em uma variavel

        # instanciando os dados na tabela
        sintomas = Sintomas(
            nome = nome,
            sintomas = sintomas
        )

        # salvando os dados
        db.session.add(sintomas) # adicionando os dados

        # salvando "literalmente"
        db.session.commit()

        
    return render_template('menu.html')

# criando a rota diagnosticos
@app.route('/consultas/')
def consultas():
    context = {}
    # verificando se a requisão é do tipo get, que por padrao é.
    if request.method == 'GET':
        busca = request.args.get('busca', None ) # aqui eu pego o que tá na barra de busca e devolvo como variavel
        context.update({'busca' : busca}) # atualizando o dicionario

    return render_template('consultas.html', context=context)