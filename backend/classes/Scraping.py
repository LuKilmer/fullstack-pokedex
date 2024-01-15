from bs4 import BeautifulSoup
import requests

class Scraping:
    @staticmethod
    def extrair_html_pokemon(nome):
        print(f"A classe extrai o pokemon {nome}.")

    @staticmethod
    def obter_html(url):
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            html = resposta.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except Exception as e:
            print(e)