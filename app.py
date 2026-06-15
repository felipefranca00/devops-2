from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Sistema de Gestão de Biblioteca web"


@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato do sistema"

@app.route("/localização")
def localizacao():
    return "Página de localização da fatec"

@app.route("/cadastro-livro")
def cadastro_livro():
    return "Formulário de cadastro de livros"


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
