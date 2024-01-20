from classes.Scraping import Scraping
from classes.Extrator import Extrator
import json
import os

class Repository:
    def __init__(self):
        self.pokemons=[]
        self.games=[
            'gold-silver-crystal',
            'red-blue-yellow',
            'firered-leafgreen',
            'ruby-sapphire-emerald',
            'platinum',
            'heartgold-soulsilver',
            'black-white',
            'black-white-2'
        ]
        self.pokemons_json=[]

    def get_imgs_from_file(self, id_game):
        nome_arquivo = f"./data/images/{self.games[id_game]}"
        lista_de_imgs = []
        tamanholista = len(os.listdir(nome_arquivo))
        for i in range(tamanholista):
            lista_de_imgs.append(f"data/images/{self.games[id_game]}/poke{i+1}.png")
        return lista_de_imgs


    def get_json_from_file(self, id_game):
        caminho_arquivo = f"./data/json/{self.games[id_game]}/data.json"
        with open(caminho_arquivo, 'r') as arquivo:
            dado_json = json.load(arquivo)
        return dado_json

    def verificar_repositorio(self,link):
        if not os.path.exists(link):
            os.makedirs(link)

    def concatenar_dados(self, imagens_do_banco,dados_json_do_banco):
        for i in range(len(dados_json_do_banco)):
            dados_json_do_banco[i]['img']=f"/imagem/{i}"
        return dados_json_do_banco

    def get_json_from_name(self, game_name):
        try:
            
            nome_arquivo = f"./data/json/{game_name}"
            self.pokemons_json.clear()
            for pokemon in self.pokemons:
                self.pokemons_json.append(pokemon.get_json_simples())
            self.verificar_repositorio(nome_arquivo)
            with open(nome_arquivo+"/data.json", 'w') as f:
                json.dump(self.pokemons_json, f)
        except Exception as e:
            print(e)
        

    def save_img(self, game_name, imgs_list):
        try:
            nome_arquivo = f"./data/images/{game_name}"
            self.verificar_repositorio(nome_arquivo)
            print("taxa de carregamento: 0%")
            for i in range(len(imgs_list)):
                resposta = Scraping.get_imgs(imgs_list[i])
                with open(f"{nome_arquivo}/poke{i+1}.png",'wb') as arquivo:
                    arquivo.write(resposta)
                taxa_de_carregamento = (i + 1) / len(imgs_list) * 100
                print(f"taxa de carregamento: {taxa_de_carregamento:.2f}%")
        except Exception as e:
            print(e)

    def pokemons_por_jogo(self, id_game:int):
        try:
            if(id_game>len(self.games)-1 or id_game<0):
                raise Exception("id informado é inválido")
            url = "https://pokemondb.net/pokedex/game/" + self.games[id_game]
            elemento_html = Scraping.obter_html(url)
            self.pokemons, imgs_list = Extrator.get_class_pokemon_por_html(elemento_html)
            self.get_json_from_name(self.games[id_game])
            self.save_img(self.games[id_game],imgs_list)
            return True
        
        except Exception as e:
            print("Aconteceu um erro no processo de extração de nomes por jogo")
            print(e.args)
            return False
        
    def exibir_pokemons_armazenados(self):
        if(len(self.pokemons)==0):
            print("Sem pokemons catalogados")
        else:
            for pokemon in self.pokemons:
                print(str(pokemon))

    def findPokemonNaLista(self, nome):
        for pokemon in self.pokemons:
            if(nome.lower() == (pokemon.nome).lower()):
                return True
        return False

    def getPokemon(self,nome):
        try:
            if(self.findPokemonNaLista(nome)):
                url = "https://pokemondb.net/pokedex/" + nome
            
                elemento_html = Scraping.obter_html(url)
                pokemon = Extrator.get_dados_pokemon(elemento_html)
                return pokemon
            else:
                return False
            
        except Exception as e:
            print(f"Aconteceu um erro no processo de extração de dados por pokemon\nPokemon com o erro: {nome}")
            print(e.args)
            return False