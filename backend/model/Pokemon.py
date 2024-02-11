from model.Move import Move




class Pokemon:
    def __init__(self,id, nome, tipo1, tipo2=None):
        self.id=id
        self.nome=nome
        self.tipo1=tipo1
        self.tipo2=tipo2
        self.move_levelup_id = []
        self.status = []
        self.egg_group=[]
        self.ev_extra=None
        self.catch_rate=0
        self.xp_base=0
        self.egg_cycle=0
        self.extra_id=[]
        self.peso=0
        self.altura=0
        self.habilidades=[]
        self.hidden_habilidades=[]
        self.genero={"male":0,"female":0}
        self.especie=None
        self.base_amizade=0


    
    def getNome(self):
        return self.nome

    def set_status(self, status):
        self.status = status


    def insert_move_levelup(self, move):
        if(move != None):
            self.move_levelup.append(move)

    def set_data(self, peso,altura, habilidades, hidden_habilidades,extra_id,especie):
        self.peso = peso
        self.altura = altura
        self.habilidades = habilidades
        self.hidden_habilidades = hidden_habilidades
        self.extra_id = extra_id
        self.especie = especie
        
    def get_data(self):
        print(
            self.peso,
            self.altura,
            self.habilidades ,
            self.hidden_habilidades ,
            self.extra_id,
            self.especie 

        )

    def set_breeeding(self, egg_group, egg_cycle , genero):
        self.egg_group = egg_group
        self.egg_cycle = egg_cycle
        self.genero = genero

    def get_breeding(self):
        print("breeding status")
        print(
            self.egg_group,
            self.egg_cycle,
            self.genero
        )

    def set_training(self, ev_extra, catch_rate, xp_base, base_amizade):
        self.ev_extra = ev_extra
        self.catch_rate = catch_rate
        self.xp_base = xp_base
        self.base_amizade = base_amizade

    def get_training(self):
        print("training status")
        print(
        self.ev_extra ,
        self.catch_rate ,
        self.xp_base ,
        self.base_amizade
        )

    def show_status(self):
        for i in self.status:
            print(i)

    def get_json_simples(self):
        pokemon={}
        tipo = []
        tipo.append(self.tipo1)
        if(self.tipo2!=None):
            tipo.append(self.tipo2)
        pokemon["id"]=self.id
        pokemon["nome"]= self.nome
        pokemon['tipo']=tipo
        return pokemon

    def get_json_complete(self):
        pass


    def __str__(self):
        if(self.tipo2):
            return f"id: {self.id} |nome: {self.nome} |tipo: {self.tipo1}, {self.tipo2}"
        else:
            return f"id: {self.id} |nome: {self.nome} |tipo: {self.tipo1}"