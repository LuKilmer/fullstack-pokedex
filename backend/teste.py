from classes.Repository import Repository


repo = Repository()
entrada=input()
while(entrada!="no"):
    print(repo.extract_complete_data_pokemon(entrada.title()))
    entrada=input()