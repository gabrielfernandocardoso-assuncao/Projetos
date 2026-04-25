# Projetos
aqui vai ser criado projetos utilitarios para o dia a dia, contendo flask, python, js, css, html, sqlite

# primeiros passos
    1. -> criar um ambiente virtual
        Como? no terminal "python -m venv '.venv'" (oque está entre aspas pode ser alterado, nao precisa ser oque está escrito.)
    2. -> depois de cria-lo temos que ativa-lo
        Como? no terminal "venv\Scripts\activate" 
        -> para desativar
            Como? no terminal "venv\Scripts\deactivate"
    3. -> Instalar a(s) biblioteca(s)
        -> Instalando o flask
            Como? no terminal "pip install flask"

# estrutura basica flask
    1. -> criar o arquivo principal por convensão "main.py", ideal "app.py"

# Padrao MVC
    1. -> O padrao MVC(Model-View-Controller) nada mais é que um conceito utilizado para separar cada ação dentro do flask
        I. Models -> Models. "Arquivo do banco de dados"
        II. Views -> Templates. "Pasta onde vai ficar os arquivos .html(paginas) que serão renderizados.
        III. Controllers -> Routes/Views. "arquivo onde vai ficar as rotas(url) do app", o nome depende do contexto, mas por convensão vai ser Views.
    2. -> Metodos GET e POST
        I. Requisição GET: O usuario pede um dado para o servidor e transmite na tela (pode ou nao acessar o banco de dados.) Ex: eu quero acessar a pagina "X"
        II. Requisição POST: o usuario envia dados para o servidor, conceito CRUD.

# Estruturando o projeto
    1. -> a estrutura fica da seguinte forma
        pasta Meu projeto/
            -> pasta "app/"
                -> pasta "static/"
                    -> pasta "css/"
                    -> pasta "js/"
                    -> pasta "img/"
                -> pasta "templates/"
                    -> arquivos ".html"
                    -> arquivo "base.html"
                -> arquivo "__init__.py"
                -> arquivo "forms.py"
                -> arquivo "models.py"
                -> arquivo "routes.py"
            -> arquivo "main.py" # por convensão "app.py"
    2. -> aplicando os conceitos no projeto
        I. realoquei o import Flask do app.py para o __init__.py
            a. importei o aplicativo no __init__.py
        II. realoquei as rotas do arquivo app.py para o views.py
            a. importei o aplicativo na view.py
            b. no __init__ para evitar erro de url eu importei a view do views.py
        III. importei no views a classe render template
            a. passei o template index.html para renderizar na função.
            b. transformei o index no base
            c. criei o index novamente
            d. renderizei o arquivo index na função da homepage
    3. -> Aplicando conceitos de routing
        I. na views.py eu crio outra view de acesso ao menu, vendo que o inicio vai ser uma pagina de login.
        II. import url_for dentro da views.py
            a. apliquei o url_for no index.
    4. -> Preparando o app para trabalhar com o banco de dados
        I.instalando as biliotecas
            a. pip install Flask-SQLAlchemy Flask-Migrate
            b. importar as ferramentas no init
                1. configurando elas no init
            c. criei o arquivo models.py no projeto
            d. crio a tabela no models e depois importo ela no init
            e. crio o arquivo wsgi
        II. Criando banco de dados
            a. flask db init
        III. salvando os dados
            a. flask db migrate -m "msg" # dentro das aspas a mensagem, é igual ao commit
                depois
            b. flask db upgrade

# forms 1
    1. -> apos direcionar o botao pesquisa para a pagina consultas, eu começo a criar o formulario do tipo get
    2. -> importo o request, para validar o tipo de formulario
    3. -> valido o tipo get para consultas e valido o tipo post para a consulta
    4. -> importo o db (banco) na views para salvar os dados recuperados do tipo post
    5. -> recupero os dados passando para variaveis com o request.form(nomedoinput)
    6. -> salvo os dados instanciando-os na classe da tabela, depois uso o comando db.session.add(nomedatabela), depois envio os dados para o banco com o comando db.session.commit().


