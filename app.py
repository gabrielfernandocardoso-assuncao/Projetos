# importando o aplicativo
from usb import app

if __name__ == "__main__": # aqui fala "se a chamada for desse arquivo, ele vai rodar o app." 
    app.run(debug=True) # nao recomendado pois pode rodar em um lugar errado, o debug diz que toda vez que fizer uma alteração no codigo, o site vai atualizar tambem

