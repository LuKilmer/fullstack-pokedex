

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

class Move:
    def __init__(self, nome, tipo, categoria, poder, acertabilidade,pp, descricao):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.poder = poder
        self.acertabilidade = acertabilidade
        self.pp = pp
        self.descricao = descricao

    def __str__(self):
        part1=f"{YELLOW}Nome:{RESET} {self.nome}{YELLOW}| Tipo : {RESET}{self.tipo}{YELLOW}| Categoria: {RESET}{self.categoria}\n"
        part2=f"{YELLOW}Poder: {RESET}{self.poder}{YELLOW}| Acertabilidade:{RESET} {self.acertabilidade}{YELLOW}| PP: {RESET}{self.pp}\n"
        
        return part1+part2+f"{YELLOW}Efeito: {RESET}{self.descricao}\n"