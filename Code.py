from bs4 import BeautifulSoup
import requests

url = "https://es.wikipedia.org/wiki/Historia_de_Bogot%C3%A1"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

contenido = soup.find('div', class_='mw-parser-output')
parrafos = contenido.find_all('p')
for p in parrafos[:3]: 
    print(p.text)