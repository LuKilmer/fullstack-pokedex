from bs4 import BeautifulSoup, Tag
from model.Pokemon import Pokemon

class Extrator:

    @staticmethod
    def extrair_status(nome):
        print(f" status do {nome} foi extraido com sucesso")

    @staticmethod
    def get_nome_por_html(elemento_html: BeautifulSoup):
        nomes = []
        tag_html = elemento_html.find_all('a', class_='ent-name')
        if tag_html:
            for tag_com_classe in tag_html:
                conteudo_tag = tag_com_classe.text
                nomes.append(conteudo_tag)
            return nomes
        else:
            raise Exception('Erro ao extrair nome do elemento html')
        
    @staticmethod
    def get_data_pokemon(elemento_html: BeautifulSoup, pokemon : Pokemon):
        tag_html = elemento_html.find('main', id='main').find_all('table',class_="vitals-table")
        Extrator.get_breeding_data(pokemon,tag_html[2])
        Extrator.get_training_data(pokemon,tag_html[1])
        Extrator.get_base_data(pokemon,tag_html[0])
        data_tables = elemento_html.find('main', id='main').find_all('table',class_="data-table")
        print(len(data_tables))
        
        Extrator.get_move_names(data_tables[0])

        Extrator.get_move_names(data_tables[1])
        Extrator.get_move_names(data_tables[2])
        #status_list =  Extrator.get_status(tag_html)
        #pokemon.set_status(status_list)
        #pokemon.show_status()
        return pokemon

    @staticmethod
    def get_move_names(data_table):
        componentes=data_table.find_all('tr')
        for i in range(len(componentes)):
            print(f"{i}: {componentes[i].text}")


    @staticmethod
    def get_base_data(pokemon: Pokemon, tag_html: Tag):
        componentes = tag_html.find_all("td")
        flag = True
        extra_id = []
        suport = ""
        for aux in componentes[6]:
            if flag:
                if aux.name == "small":
                    suport+=aux.text
                    flag=False
                    extra_id.append(suport)
                    suport=""
                else:
                    suport+=aux
            else:
                flag=True
        especie = componentes[2].text
        altura = componentes[3].text.split(" ")[0].replace("\xa0","")
        peso = componentes[4].text.split(" ")[0].replace("\xa0","")
        habilidades=[]
        hidden_habilidades=[]
        for ind in componentes[5].find_all("small"):
            hidden_habilidades.append(ind.text.split(" (")[0])
        for ind in componentes[5].find_all("a"):
            if  ind.text not in hidden_habilidades:
                habilidades.append(ind.text)
        pokemon.set_data(peso,altura,habilidades,hidden_habilidades,extra_id,especie)
        
    
    @staticmethod
    def get_breeding_data(pokemon: Pokemon, tag_html: Tag):
        egg_group=[]
        genero={"male":0,"female":0}
        componentes = tag_html.find_all('td')
        for group in componentes[0].find_all('a'):
           egg_group.append(group.text)
        for aux in componentes[1].find_all('span'):
           genero[aux.text.split("% ")[1]] = aux.text.split("% ")[0]
        egg_cycle = componentes[2].text.split(" ")[0]
        pokemon.set_breeeding(egg_group, egg_cycle ,genero)
        
    
    @staticmethod
    def get_training_data(pokemon: Pokemon, tag_html: Tag):
        componentes= tag_html.find_all('td')
        extra_ev = componentes[0].text.split("\n")[1]
        catch_rate = componentes[1].text.split(" ")[0].split("\n")[1]
        base_amizade = componentes[2].text.split(" ")[0].split("\n")[1]
        base_xp = componentes[3].text.split("\n")[0]
        pokemon.set_training(extra_ev,catch_rate,base_xp,base_amizade)

    @staticmethod
    def get_status(tag_html):
        status = tag_html.find_all('table',class_="vitals-table")[3]
        status_nome = status.find_all('th')
        status_num = status.find_all('td', class_="cell-num")
        status_list = []
        for i in range(6):
            attribute_status ={"nome":{status_nome[i].text.replace(" ","_")},"base":{status_num[i*3].text},"low":{status_num[i*3+1].text},"high":{status_num[i*3+2].text}}
            status_list.append(attribute_status)
        return status_list


    @staticmethod
    def get_data_complete(element_html: BeautifulSoup):
        tag_html = element_html.find('main', id='main')
        nome = tag_html.find('h1')
        status = tag_html.find_all('table',class_="vitals-table")[3]
        status_nome = status.find_all('th')
        status_num = status.find_all('td', class_="cell-num")
        
        status_list = []
        for i in range(6):
            attribute_status ={"nome":{status_nome[i].text.replace(" ","_")},"base":{status_num[i*3].text},"low":{status_num[i*3+1].text},"high":{status_num[i*3+2].text}}
            status_list.append(attribute_status)
        
        pokemon = Pokemon(2,nome,"glass")
        pokemon.setStatus(status_list)
        pokemon.showStatus()



    @staticmethod
    def get_class_pokemon_por_html(elemento_html: BeautifulSoup):
        pokemons = []
        id = 1
        nome = ""
        tipo1 = ""
        tipo2 = ""
        tag_html = elemento_html.find_all('div', class_='infocard')
        imgs_links = []
        if tag_html:
            for tag_com_classe in tag_html:

                tag_nome = tag_com_classe.find('a', class_='ent-name')
                img_tag = tag_com_classe.find('img', class_='img-sprite')
                imgs_links.append(img_tag.get('src'))
                if(tag_nome):
                    nome = tag_nome.text
                else:
                    raise Exception('Erro ao extrair nome do elemento html')

                tag_types = tag_com_classe.find_all('a', class_='itype')
                
            
                if(len(tag_types)==1):
                    tipo1 = tag_types[0].text
                    poke = Pokemon(id, nome, tipo1)
                    pokemons.append(poke)
                    id+=1
                elif(len(tag_types)==2):
                    tipo1 = tag_types[0].text
                    tipo2 = tag_types[1].text
                    poke = Pokemon(id, nome, tipo1, tipo2)
                    pokemons.append(poke)
                    id+=1
                else:
                    raise Exception('Erro ao extrair tipo do elemento html')

            return pokemons, imgs_links
        else:
            raise Exception('Erro ao extrair pokemon do elemento html')

        