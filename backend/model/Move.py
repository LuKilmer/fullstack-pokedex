class Move:
    def __init__(self, nome, tipo, categoria, poder, acertabilidade,pp):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.poder = poder
        self.acertabilidade = acertabilidade
        self.pp = pp

    def __str__(self):
        return f"{self.nome}|{self.tipo}|{self.categoria}|{self.poder}|{self.acertabilidade}|{self.pp}"