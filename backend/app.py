from flask import Flask, render_template, send_file, jsonify
from classes.Repository import Repository

import json

app = Flask(__name__)
repo = Repository()



dados_json_do_banco = [{"chave": "valor1"}, {"chave": "valor2"}]

game = 1

imagens_do_banco = repo.get_imgs_from_file(game)

dados_json_do_banco = repo.get_json_from_file(game)
dados = repo.concatenar_dados(imagens_do_banco,dados_json_do_banco)
print(dados)
@app.route('/')
def index():
    return render_template('./index.html', dados_json = dados)
    #return render_template('./index.html', imagens=imagens_do_banco, dados_json=dados_json_do_banco)

@app.route('/imagem/<int:indice>')
def obter_imagem(indice):
    return send_file(imagens_do_banco[indice], mimetype='image/png')

@app.route('/json/<int:indice>')
def obter_json(indice):
    return jsonify(dados_json_do_banco[indice])

if __name__ == '__main__':
    app.run(debug=True)