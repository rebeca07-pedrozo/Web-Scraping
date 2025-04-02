import xml.etree.ElementTree as ET
import requests
import pandas as pd
import pickle

url = "https://sdmx.oecd.org/public/rest/data/OECD.ELS.SAE,DSD_LFS@DF_LFS_COMP,1.1/all?startPeriod=2019&dimensionAtObservation=AllDimensions"

response = requests.get(url)

if response.status_code == 200:
    print(" Conexión exitosa con la API")
    
    root = ET.fromstring(response.content)
    
    print(f"Primer Tag XML: {root.tag}")
    
    records = []
    for obs in root.findall(".//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}Obs"):
        value = obs.find("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsValue").attrib["value"]
        dimensions = obs.findall(".//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}Value")
        
        print(f"Dimensiones encontradas: {[d.attrib for d in dimensions]}")

        year = dimensions[0].attrib["value"] if len(dimensions) > 0 else "Desconocido"
        country = dimensions[1].attrib["value"] if len(dimensions) > 1 else "Desconocido"
        
        records.append({"Año": year, "País": country, "Valor": float(value)})
    
    df = pd.DataFrame(records, columns=["Año", "País", "Valor"])
    print(df.head())  
    
    with open("datos_oecd.pkl", "wb") as f:
        pickle.dump(records, f)
    
    print(" Datos guardados correctamente en 'datos_oecd.pkl'")

else:
    print(" Error al conectar con la API")

