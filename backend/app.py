from flask import Flask, render_template,current_app, url_for, send_file, jsonify, request, Response
from classes.Repository import Repository
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


repo = Repository()




game = 0

erro_json = repo.get_erro_json()
imagens_do_banco = repo.get_imgs_from_file(game)
dados_json_do_banco = repo.get_json_from_file(game)
dados = repo.concatenar_dados(dados_json_do_banco)

@app.route('/', methods=['GET'])
def index():
    #return render_template('./index.html', dados_json = dados)
    #return render_template('./index.html', imagens=imagens_do_banco, dados_json=dados_json_do_banco)
    valid_ids={}
   
    valid_ids["id"]=[0,1,2,3,4,5,6,7]
    return jsonify(valid_ids)

@app.route('/pokedex/<int:indice>', methods=['GET'])
def index_by_game(indice):
    
    #return render_template('./index.html', dados_json = dados)
    #return render_template('./index.html', imagens=imagens_do_banco, dados_json=dados_json_do_banco)
    if(indice<8):
        dados_json_do_banco = repo.get_json_from_file(indice)
        
       
        dados = Repository.concatenar_dados(indice, dados_json_do_banco)
    
        return jsonify(dados),200
    else:
        return jsonify(erro_json),404


@app.route('/pokedex/<int:indice>/imagem/<int:id>', methods=['GET'])
def obter_imagem(indice, id):
    with current_app.app_context():
        imagens_do_banco = repo.get_imgs_from_file(indice)
        print(len(imagens_do_banco))
        if(id<len(imagens_do_banco)):
            return send_file(imagens_do_banco[id], mimetype='image/png')
        else:
            return "Imagem não encontrada", 404
   




@app.route('/pokedex/<int:indice>/pokemon/<int:id>', methods=['GET'])
def obter_json(indice, id):
    if(indice<8):
        dados_json_do_banco = repo.get_json_from_file(indice)
        dados = repo.concatenar_dados(dados_json_do_banco)
        if(len(dados)>id):
             return jsonify(dados_json_do_banco[id]), 200
        else:
            return jsonify(erro_json),404
    else:
        return jsonify(erro_json),404
    

if __name__ == '__main__':
    app.run(debug=True)