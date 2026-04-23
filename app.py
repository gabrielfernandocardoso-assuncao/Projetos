# importando do pacote flask a classe Flask
from flask import Flask

# startando o aplicativo
app = Flask(__name__) # ele vai iniciar o aplicativo com base nesse arquivo.

# passando uma rota
@app.route('/') # rotas sao passadas entre "/"
def homepage(): # função de renderização 

    return "homepage" # renderizando uma string

if __name__ == "__main__": # aqui fala "se a chamada for desse arquivo, ele vai rodar o app." 
    app.run(debug=True) # nao recomendado pois pode rodar em um lugar errado, o debug diz que toda vez que fizer uma alteração no codigo, o site vai atualizar tambem

