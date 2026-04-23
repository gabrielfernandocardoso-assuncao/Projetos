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