from flask  import Flask


app = Flask(__name__) # O flask recomenda que você use o nome "app" como nome

# Primeira página do site

# Quando você começa com "@", se torna um decorator. Basicamente, abaixo está falando que a função "homepage" vai ser exibita na home (página inicial)
@app.route("/") # É a rota do site, basicamente o link do site.
def homepage():
    return "Este é meu primeiro site usando Python/Flask" # Retorna o que eu quero que exiba na página

# Subir o site
app.run(debug = True) # Carrega o site