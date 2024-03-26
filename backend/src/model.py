class Pokemon:
    def __init__(self, id, nome, tipo1, tipo2=None):
        self.id = id
        self.nome = nome
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.catch_rate = 0
        self.xp_base = 0
        self.ciclo_de_incubatorio = 0
        self.peso = 0
        self.altura = 0
        self.base_amizade = 0
        self.genero = None
        self.especie = None
        self.ev_extra = None
        self.habilidades_ocultas = []
        self.habilidades = []
        self.extra_id = []
        self.movimentos_por_levelUp = []
        self.status = {
            "hp":0,
            "atk":0,
            "def":0,
            "sp_atk":0,
            "sp_def":0,
            "speed":0
        }
        self.grupo_de_ovos = []
    
    def get_nome(self):
        return self.nome

    def set_status(self, status):
        self.status = status

    def add_movimento_por_levelUp(self, Movimento):
        if(Movimento != None):
            self.Movimento_levelup.append(Movimento)

    def set_data_base(self, peso,altura, habilidades, habilidades_ocultas,extra_id,especie):
        self.peso = peso
        self.altura = altura
        self.habilidades = habilidades
        self.habilidades_ocultas = habilidades_ocultas
        self.extra_id = extra_id
        self.especie = especie

    def set_dados_procriacao(self, grupo_de_ovos, ciclo_de_incubatorio , genero):
        self.grupo_de_ovos = grupo_de_ovos
        self.ciclo_de_incubatorio = ciclo_de_incubatorio
        self.genero = genero

    def set_dados_treinamento(self, ev_extra, catch_rate, xp_base, base_amizade):
        self.ev_extra = ev_extra
        self.catch_rate = catch_rate
        self.xp_base = xp_base
        self.base_amizade = base_amizade

    def show_status(self):
        for i in self.status:
            print(i)

    def get_json_simples(self):

        pokemon = {}
        tipo = []
        tipo.append(self.tipo1)

        if(self.tipo2 != None):
            tipo.append(self.tipo2)

        pokemon["id"] = self.id
        pokemon["nome"] = self.nome
        pokemon['tipo'] = tipo

        return pokemon

    def get_json_complete(self):
        pass


class Movimento:
    def __init__(self, nome, tipo, categoria, poder, acertabilidade,pp, descricao):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.poder = poder
        self.acertabilidade = acertabilidade
        self.pp = pp
        self.descricao = descricao