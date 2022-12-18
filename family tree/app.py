# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Marco Antonio" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():
    
    nome = "Antonio Marcos"
    idade = 47
    
    return render_template('pai.html' , nome = nome , idade = idade)      

# defina a rota para a página da mãe
@app.route("/mae")
def mae():
    
    nome = "Danielle"
    idade = 41
    
    return render_template('mae.html' , nome = nome , idade = idade)      

# adicione outras rotas, se você quiser
@app.route("/irmao")
def irmao1():
    
    nome = "Marco Andre"
    idade = 2
    
    return render_template('irmao.html' , nome = nome , idade = idade)      

@app.route("/irmao2")
def irmao2():
    
    nome = "Marco Aurelio"
    idade = 10
    
    return render_template('irmao2.html' , nome = nome , idade = idade)      





# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
