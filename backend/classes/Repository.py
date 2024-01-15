from classes.Scraping import Scraping
from classes.Extrator import Extrator

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
    def pokemons_por_jogo(self, id_game:int):
        try:
            if(id_game>len(self.games)-1 or id_game<0):
                raise Exception("id informado é inválido")
            url = "https://pokemondb.net/pokedex/game/" + self.games[id_game]
            print(url)
            elemento_html = Scraping.obter_html(url)
            self.pokemons = Extrator.get_class_pokemon_por_html(elemento_html)
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