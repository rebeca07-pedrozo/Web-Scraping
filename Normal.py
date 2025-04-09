from bs4 import BeautifulSoup
import requests

url = "https://www.dosquebradas.gov.co/web/index.php/dosquebradas/ciudad/sala-de-prensa/noticias/301-vigencia-2025/8099-la-alcaldia-de-dosquebradas-y-la-universidad-libre-unen-esfuerzos-para-asistir-juridicamente-a-la-comunidad"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

contenido = soup.find('div', class_='item-page')  

if contenido:
    parrafos = contenido.find_all('p')  
    for p in parrafos[:3]:  
        print(p.text.strip())
else:
    raise Exception("No se encontró el contenido en la página HTML. Verifica la estructura del sitio.")

