from bs4 import BeautifulSoup
import requests

url = "https://concepto.de/definicion/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

contenido = soup.find('div', class_='text-container')  

if contenido:
    parrafos = contenido.find_all('p')
    for p in parrafos[:3]: 
        print(p.text)
else:
    raise Exception("No se encontró el contenido en la página HTML. Verifica la estructura del sitio.")
