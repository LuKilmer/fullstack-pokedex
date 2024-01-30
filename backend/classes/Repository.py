from classes.Scraping import Scraping
from classes.Extrator import Extrator
from classes.TesterRepository import TesterRepository
import json
import os

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN   = "\033[1;32m"  
YELLOW  = "\033[1;33m"
ROSA  = "\033[1;35m"
ROXO = "\033[0;35m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
separeted="'"

class Repository:
    def __init__(self):
        self.pokemons=[
            {'gold-silver-crystal':[]},
            {'red-blue-yellow':[]},
            {'firered-leafgreen':[]},
            {'ruby-sapphire-emerald':[]},
            {'platinum':[]},
            {'heartgold-soulsilver':[]},
            {'black-white':[]},
            {'black-white-2':[]},
        ]
        self.pokemons_json=[
            {'gold-silver-crystal':[]},
            {'red-blue-yellow':[]},
            {'firered-leafgreen':[]},
            {'ruby-sapphire-emerald':[]},
            {'platinum':[]},
            {'heartgold-soulsilver':[]},
            {'black-white':[]},
            {'black-white-2':[]},
        ]
        self.start_server_repository()

    def start_server_repository(self):
        try:
            list_of_problems = self.check_file_integrity(self)
            if(list_of_problems):
                pass
            else:
                pass
        except Exception as e:
            raise Exception(f"{RED}ERRO AO ARQUIVOS{RESET}")
        
    def check_file_integrity(self):
        #numero de nomes e repetições
        #esses nomes estão nos arquivos json e id unico
        return True


    def get_imgs_from_file(self, id_game):
        game_name = self.pokemons[id_game].keys().__str__().split(separeted)[1]
        nome_arquivo = f"./data/images/{game_name}"
        lista_de_imgs = []
        tamanholista = len(os.listdir(nome_arquivo))
        for i in range(tamanholista):
         
            lista_de_imgs.append(f"./data/images/{game_name}/poke{i+1}.png")
        return lista_de_imgs
    

    def get_erro_json(self):
        caminho_arquivo = f"./data/json/erro.json"
        with open(caminho_arquivo, 'r') as arquivo:
            dado_json = json.load(arquivo)
        return dado_json


    def load_all_from_games(self):

        for i in range(len(self.games)):
            self.pokemons.clear()
            print(f"{RED} Os dados do jogo {self.games[i]} serão salvos {RESET}")
            self.pokemons_por_jogo(i)
            print(f"{GREEN}Os dados do jogo {self.games[i]} foram salvos {RESET}")
   
    

    def get_json_from_file(self, id_game):
        
        caminho_arquivo = f"./data/json/{self.pokemons[id_game].keys().__str__().split(separeted)[1]}/data.json"
        with open(caminho_arquivo, 'r') as arquivo:
            dado_json = json.load(arquivo)
        return dado_json
    

    def verificar_repositorio(self,link):
        if not os.path.exists(link):
            os.makedirs(link)

    def concatenar_dados(indice : int, dados_json_do_banco: str):
        base_url = f"http://127.0.0.1:5000/pokedex/{indice}/"
        for i in range(len(dados_json_do_banco)):
            dados_json_do_banco[i]['img']=f"{base_url}/imagem/{i}"
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
            print(f"{ROSA}taxa de carregamento:{RESET}{RED} 0%{RESET}")
            for i in range(len(imgs_list)):
                resposta = Scraping.get_imgs(imgs_list[i])
                with open(f"{nome_arquivo}/poke{i+1}.png",'wb') as arquivo:
                    arquivo.write(resposta)
                taxa_de_carregamento = (i + 1) / len(imgs_list) * 100
                nome = imgs_list[i].split("/")[6].split(".")[0]
                
                print(f"{YELLOW}{nome.title()}{RESET}{ROSA} taxa de carregamento: {RESET}{RED}{taxa_de_carregamento:.2f}%{RESET}")
        except Exception as e:
            print(e)

    def pokemons_by_games(self, id_game):
        try:
            game_name = self.pokemons[id_game].keys().__str__().split(separeted)[1]
            if(id_game>len(self.games)-1 or id_game<0):
                raise Exception("id informado é inválido")
            url = "https://pokemondb.net/pokedex/game/" + game_name
            elemento_html = Scraping.obter_html(url)
            self.pokemons, imgs_list = Extrator.get_class_pokemon_por_html(elemento_html)
            self.get_json_from_name(game_name)
            self.save_img(game_name,imgs_list)
            return True
        
        except Exception as e:
            print(f"{RED}Aconteceu um erro no processo de extração de nomes por jogo{RESET}")
            print(e.args)
            return False
        
    def show_stored_pokemons(self):
        if(len(self.pokemons)==0):
            print("Sem pokemons catalogados")
        else:
            for pokemon in self.pokemons:
                print(str(pokemon))

    def find_pokemon_in_list(self, nome):
        for pokemon in self.pokemons:
            if(nome.lower() == (pokemon.nome).lower()):
                return True
        return False
    
    def load_names_by_json(self):
        for i in range(len(self.pokemons_json)):
            self.pokemons_json[i] = self.get_json_from_file(i)
        for i in range(len(self.pokemons_json)):
            print(len(self.pokemons_json[i]))

    def get_pokemon(self,nome):
        try:
            if(self.findPokemonNaLista(nome)):
                url = "https://pokemondb.net/pokedex/" + nome
            
                elemento_html = Scraping.obter_html(url)
                pokemon = Extrator.get_dados_pokemon(elemento_html)
                return pokemon
            else:
                return False
            
        except Exception as e:
            print(f"{RED}Aconteceu um erro no processo de extração de dados por pokemon\nPokemon com o erro: {nome}{RESET}")
            print(e.args)
            return False