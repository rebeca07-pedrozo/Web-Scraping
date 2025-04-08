import csv
import requests
from bs4 import BeautifulSoup

def obtener_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        respuesta = requests.get(url, headers=headers, timeout=10)
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            print(f"Error al obtener la página: código {respuesta.status_code}")
            return None
    except Exception as e:
        print(f"Excepción al obtener la página: {e}")
        return None

def extraer_titulos(html):
    soup = BeautifulSoup(html, 'html.parser')
    titulos = []

    for heading in soup.find_all(['h1', 'h2', 'h3']):
        if heading.text.strip() and len(heading.text.strip()) > 15:
            titulos.append(heading.text.strip())

    for elemento in soup.select('title, .headline, .article-title, .news-title'):
        if elemento.text.strip() and elemento.text.strip() not in titulos:
            titulos.append(elemento.text.strip())

    return titulos

def extraer_articulos(html):
    soup = BeautifulSoup(html, 'html.parser')
    articulos = []

    for articulo_elem in soup.select('article, .article, .post, .news-item'):
        articulo = {}

        titulo_elem = articulo_elem.find(['h1', 'h2', 'h3']) or articulo_elem.select_one('.title, .headline')
        if titulo_elem:
            articulo['titulo'] = titulo_elem.text.strip()
        else:
            continue

        fecha_elem = articulo_elem.select_one('.date, .time, .published, .timestamp')
        articulo['fecha'] = fecha_elem.text.strip() if fecha_elem else ""

        resumen_elem = articulo_elem.select_one('.summary, .excertp, .description, .snippet, p')
        articulo['resumen'] = resumen_elem.text.strip() if resumen_elem else ""

        articulos.append(articulo)

    return articulos

while True:
    print("\n=== Web Scraper ===")
    url = input("Ingresa la URL del artículo o sitio web: ")
    html = obtener_html(url)

    if not html:
        print("No se pudo obtener contenido. ¿Intentar de nuevo? (s/n)")
        if input().lower() != 's':
            break
        else:
            continue

    print("\n¿Qué deseas hacer?")
    print("1. Extraer solo los títulos")
    print("2. Extraer artículos completos")
    opcion = input("Selecciona una opción (1 o 2): ")

    datos = []

    if opcion == '1':
        datos = extraer_titulos(html)
    elif opcion == '2':
        datos = extraer_articulos(html)
    else:
        print("Opción inválida.")
        continue

    print("\n¿Deseas guardar los datos?")
    print("1. Sí, guardar en archivo CSV")
    print("2. No, solo mostrarlos por consola")
    opcion_guardado = input("Selecciona una opción (1 o 2): ")

    if opcion_guardado == '1':
        nombre_archivo = input("Nombre del archivo CSV (ej: datos.csv): ")
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if opcion == '1':
                writer.writerow(['Titulo'])
                for titulo in datos:
                    writer.writerow([titulo])
            else:
                writer.writerow(['Titulo', 'Fecha', 'Resumen'])
                for articulo in datos:
                    writer.writerow([articulo['titulo'], articulo['fecha'], articulo['resumen']])
        print(f"\nDatos guardados en {nombre_archivo}")
    else:
        print("\nMostrando los datos por consola:")
        if opcion == '1':
            for i, titulo in enumerate(datos, start=1):
                print(f"{i}. {titulo}")
        else:
            for i, articulo in enumerate(datos, start=1):
                print(f"\nArtículo {i}")
                print(f"Título : {articulo['titulo']}")
                print(f"Fecha  : {articulo['fecha']}")
                print(f"Resumen: {articulo['resumen']}")

    print("\n¿Deseas realizar otra búsqueda?")
    print("1. Sí, volver al inicio")
    print("2. No, salir del programa")
    repetir = input("Selecciona una opción (1 o 2): ")

    if repetir != '1':
        print("BYEEEE")
        break
