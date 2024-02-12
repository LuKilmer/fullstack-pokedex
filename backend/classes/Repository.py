from model.Pokemon import Pokemon
from classes.Scraping import Scraping
from classes.Extrator import Extrator
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
            self.load_pokemons_by_json()
            list_of_problems = self.check_file_integrity()
            if(list_of_problems):
                pass
            else:
                pass
        except Exception as e:
            print(e.args)
            print(f"{RED}ERRO AO ARQUIVOS{RESET}")
        
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

    def reload_from_game(self, game_id):
        print(self.get_json_from_file(game_id))

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
    

    def ensure_directory_exists(self,link):
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

            self.ensure_directory_exists(nome_arquivo)

            with open(nome_arquivo+"/data.json", 'w') as f:
                json.dump(self.pokemons_json, f)

        except FileNotFoundError as fnfe:
            print(f"Erro: Diretório não encontrado - {fnfe}")

        except Exception as e:
            print(f"Erro ao criar arquivo JSON: {e}")
        

    def save_images(self, game_name, imgs_list):
        try:
            directory_path = f"./data/images/{game_name}"
            self.ensure_directory_exists(directory_path)

            print(f"{ROSA}Taxa de carregamento:{RESET}{RED} 0%{RESET}")

            for i, img_url in enumerate(imgs_list, start=1):
                image_data = Scraping.get_imgs(img_url)
                filename = f"{directory_path}/poke{i}.png"

                with open(filename, 'wb') as file:
                    file.write(image_data)

                load_percentage = (i / len(imgs_list)) * 100
                pokemon_name = img_url.split("/")[6].split(".")[0]

                print(f"{YELLOW}{pokemon_name.title()}{RESET}{ROSA} Taxa de carregamento: {RESET}{RED}{load_percentage:.2f}%{RESET}")

        except Exception as e:
            print(f"Erro ao salvar imagens: {e}")


    def extract_pokemons_by_game(self, id_game):
        try:
            if id_game < 0 or id_game >= len(self.pokemons):
                raise ValueError("ID informado é inválido")

            game_name = list(self.pokemons[id_game].keys())[0]
            url = f"https://pokemondb.net/pokedex/game/{game_name}"
            
            
            html_element = Scraping.obter_html(url)
            self.pokemons, imgs_list = Extrator.get_class_pokemon_por_html(html_element)
            
           
            self.get_json_from_name(game_name)
            self.save_images(game_name, imgs_list)
            
            return True
        
        except ValueError as ve:
            print(f"{RED}Erro: {str(ve)}{RESET}")
            return False

        except Exception as e:
            print(f"{RED}Aconteceu um erro no processo de extração de nomes por jogo{RESET}")
            print(f"Detalhes do erro: {str(e)}")
            return False
        
    def show_stored_pokemons(self):
        if(len(self.pokemons)==0):
            print("Sem pokemons catalogados")
        else:
            for pokemon in self.pokemons:
                print(str(pokemon))

    def find_pokemon_in_list(self, nome):
        count = 0
        for index in range(len(self.pokemons)):
            for pokemon in self.pokemons[index][f"{self.pokemons[index].keys().__str__().split(separeted)[1]}"]:
                if pokemon.nome == nome:
                    return pokemon
        return False
            
    def extract_complete_data_pokemon(self, nome):
        try:
            pokemon = self.find_pokemon_in_list(nome)
            if pokemon:
                url = f"https://pokemondb.net/pokedex/{pokemon.nome}"
                html_element = Scraping.obter_html(url)
                pokemon = Extrator.get_data_pokemon(html_element, pokemon)
                return pokemon
            else:
                raise Exception("Pokemon não existe, ou nome está errado")

        except Exception as e:
            print(f"{RED}{e.args}{RESET}")
        
  
    def transform_json(self):
        for i in range(len(self.pokemons_json)):
            for pokemon in self.pokemons_json[i]:
                
                if(len(pokemon["tipo"])==2):
                    poke = Pokemon(pokemon["id"],pokemon["nome"],pokemon["tipo"][0],pokemon["tipo"][1])
                else:
                    poke = Pokemon(pokemon["id"],pokemon["nome"],pokemon["tipo"][0])
                self.pokemons[i][f"{self.pokemons[i].keys().__str__().split(separeted)[1]}"].append(poke)

            
        '''
        for game in self.pokemons_json:
            print(len(game))
            for pokemon in game:
                if(len(pokemon["tipo"])==2):
                    poke = Pokemon(pokemon["id"],pokemon["nome"],pokemon["tipo"][0],pokemon["tipo"][1])
                else:
                    poke = Pokemon(pokemon["id"],pokemon["nome"],pokemon["tipo"][0])
                self.pokemons.append(poke)
        '''
            
       

    def load_pokemons_by_json(self):
        try:
            if(len(self.pokemons_json)==0):
                raise Exception("Não há dados salvos nos arquivos")
            for i in range(len(self.pokemons_json)):
                self.pokemons_json[i] = self.get_json_from_file(i)
                print(f"{GREEN}Dados do jogo {self.pokemons[i].keys().__str__().split(separeted)[1]} completo{RESET}")
            self.transform_json()
        except Exception as e:
            print(f"{RED}{e.args}{RESET}")

    


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