from flask  import Flask # Importa o framework Flask
from flask import render_template # Importa a função de invocar templates


app = Flask(__name__) # O flask recomenda que você use o nome "app" como nome

# Primeira página do site

# Quando você começa com "@", se torna um decorator. Basicamente, abaixo está falando que a função "homepage" vai ser exibita na home (página inicial)
@app.route("/") # É a rota do site, basicamente o link do site.
def homepage():
    return render_template("homepage.html") # Template da homepage


@app.route("/contato")
def contatos():
     return render_template("contato.html") # Template de contato


@app.route("/usuarios/<nome_user>") # Basicamente, o que for inserido dentro "< >" será o nome do usuário
def usuarios(nome_user): # Ela recebe o nome do usuário como parâmetro em "nome_user"
    return render_template("usuarios.html", variavel_nome_html = nome_user)
    # "variavel_nome_html" é o nome da variável que foi importada no corpo do HTML
    # Segundo "nome_user" é o parâmetro utilizado na função


if __name__ == "__main__": # É necessário estar dentro desta condicional para carregar o site no servidor
    # Subir o site
    app.run(debug = True) # Carrega o site