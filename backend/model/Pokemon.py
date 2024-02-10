from model.Move import Move




class Pokemon:
    def __init__(self,id, nome, tipo1, tipo2=None):
        self.id=id
        self.nome=nome
        self.tipo1=tipo1
        self.tipo2=tipo2
        self.move_levelup_id = []
        self.status = []
    
    def getNome(self):
        return self.nome

    def setStatus(self, status):
        self.status = status


    def insert_move_levelup(self, move):
        if(move != None):
            self.move_levelup.append(move)


    def showStatus(self):
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