from model.Move import Move

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN   = "\033[1;32m"  
YELLOW  = "\033[1;33m"
PINK  = "\033[1;35m"
ROXO = "\033[0;35m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

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


    
    def get_nome(self):
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
        part1 = f"{YELLOW}Peso: {RESET}{self.peso}{YELLOW} | Altura:{RESET} {self.altura}{YELLOW} | Especie:{RESET} {self.especie}\n"
        part2 = f"{YELLOW}Habilidades:\n{RESET}"
        part3 = f"{YELLOW}Hidden Habilidades:\n{RESET}"
        part4 = f"{YELLOW}ID nos jogos:\n{RESET}"
        for i in range (len(self.habilidades)):
            part2+=f"{YELLOW}{i+1}: {RESET}{self.habilidades[i]}\n"
        for i in range (len(self.hidden_habilidades)):
            part3+=f"{YELLOW}{i+1}: {RESET}{self.hidden_habilidades[i]}\n"
        for j in self.extra_id:
            part4+=f"{YELLOW}{j[:4]} {RESET}{j[5:]}\n"
        return part1+part2+part3+part4

    def set_breeeding(self, egg_group, egg_cycle , genero):
        self.egg_group = egg_group
        self.egg_cycle = egg_cycle
        self.genero = genero

    def get_breeding(self):
        part1=f"{BLUE}male: {self.genero['male']}% {RESET}|{PINK}female: {self.genero['female']}%{RESET}\n"
        part2=f"{YELLOW}Egg cycle: {RESET}{self.egg_cycle} steps\n"
        part3=f"{YELLOW}Egg group: \n{RESET}"
        for i in range(len(self.egg_group)):
            part3+=f"{YELLOW}{i+1} - {RESET}{self.egg_group[i]}\n"
     
        return part1+part2+part3


    def set_training(self, ev_extra, catch_rate, xp_base, base_amizade):
        self.ev_extra = ev_extra
        self.catch_rate = catch_rate
        self.xp_base = xp_base
        self.base_amizade = base_amizade

    def get_training(self):
        
        part1 = f"{YELLOW}EV por batalha: {RESET}{self.ev_extra}\n"
        part2 = f"{YELLOW}Taxa de Captura: {RESET}{self.catch_rate}\n"
        part3 = f"{YELLOW}XP base: {RESET}{self.xp_base}\n"
        part4 = f"{YELLOW}Amizade base: {RESET}{self.base_amizade}\n"

        return part1+part2+part3+part4
    
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
            part1 = f"{YELLOW}id: {RESET}{self.id} {YELLOW}|nome: {RESET}{self.nome} {YELLOW}|tipo: {RESET}{self.tipo1}, {self.tipo2}\n"
        else:
            part1 = f"{YELLOW}id: {RESET}{self.id} {YELLOW}|nome: {RESET}{self.nome} {YELLOW}|tipo: {RESET}{self.tipo1}\n"
        part2 = self.get_training()
        part3 = self.get_breeding()
        part4 = self.get_data()
        return part1 + part2 + part3 +part4
        