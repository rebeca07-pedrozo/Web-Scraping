
## Web Scraping

1. Importación de librerías (Acá ya están instaladas)
```
from bs4 import BeautifulSoup
import requests
```
Explicación: 

*requests:* sirve para hacer peticiones HTTP, como cuando visitamos una página web desde tu navegador.

*BeautifulSoup:* se utiliza para analizar (parsear) el contenido HTML de las páginas web y extraer datos fácilmente.

2. Petición al sitio web
```
url = "https://www.dosquebradas.gov.co/..."
page = requests.get(url)

```
Explicación: 


Se define la URL de la página que queremos "scrapear".

Se hace la petición con requests.get(url) para obtener el contenido de esa página web.

3. Crear el objeto BeautifulSoup
```
soup = BeautifulSoup(page.text, 'html.parser')

```
Explicacion: 

page.text contiene el HTML completo de la página.

BeautifulSoup(...) convierte ese HTML en un objeto que podemos recorrer fácilmente para buscar etiquetas específicas (como div, p, etc.).

'html.parser' es el analizador que usa BeautifulSoup para leer el HTML.

4. Buscar el contenido principal de la noticia
```
contenido = soup.find('div', class_='item-page')

```
En este ejemplo, estamos buscando un div que tenga la clase item-page, que es donde está realmente el texto de la noticia.

.find() devuelve solo el primer elemento que cumple con esas condiciones.

5. Extraer los párrafos del contenido
```
if contenido:
    parrafos = contenido.find_all('p')
    for p in parrafos[:3]:
        print(p.text.strip())

```

if contenido: verifica que el div se haya encontrado correctamente.

contenido.find_all('p') busca todas las etiquetas <p> (párrafos) dentro del div.

for p in parrafos[:3]: recorre los primeros 3 párrafos solamente (puedes cambiar ese número).

print(p.text.strip()) imprime el texto dentro de cada párrafo, quitando espacios en blanco al principio y al final.

6. Excepción en caso de no encontrar ese elemento. 

