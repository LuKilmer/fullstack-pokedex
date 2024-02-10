from bs4 import BeautifulSoup
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
    def get_dados_pokemon(elemento_html: BeautifulSoup):
        tag_html = elemento_html.find('main', id='main')
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
    def get_data_complete(element_html: BeautifulSoup):
        print(element_html)



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

        