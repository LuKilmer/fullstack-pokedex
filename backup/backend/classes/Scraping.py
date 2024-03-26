from bs4 import BeautifulSoup
import requests

class Scraping:
    @staticmethod
    def extrair_html_pokemon(nome):
        print(f"A classe extrai o pokemon {nome}.")

    @staticmethod
    def get_imgs(link):
        try:
            img = requests.get(link)
            if(img.status_code == 200):
                return img.content
            else:
                raise Exception(f"ERRO AO OBTER IMAGEM DO LINK {link}")
        except Exception as e:
            print(e)


    @staticmethod
    def obter_html(url):
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            html = resposta.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except Exception as e:
            return e