# importando o aplicativo
from usb import app

# importando a função render_template
from flask import render_template

# passando uma rota
@app.route('/') # rotas sao passadas entre "/"
def homepage(): # função de renderização 

    return render_template('index.html') # renderizando uma string, renderizando um template