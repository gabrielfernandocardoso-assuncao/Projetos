# importando o aplicativo
from usb import app

# importando a função render_template, url_for
from flask import render_template, url_for

# passando uma rota
@app.route('/') # rotas sao passadas entre "/"
def homepage(): # função de renderização 

    return render_template('index.html') # renderizando uma string, renderizando um template

# criando a rota para o menu, apos o login
@app.route('/menu/')
def menu():

    return render_template('menu.html')