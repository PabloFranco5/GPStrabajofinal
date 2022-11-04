import requests

def clima(origen):
    urlclima_o = f"https://es.wttr.in/{origen}?format=j1"
    #urlclima_d = f"https://es.wttr.in/{destino}?format=j1"

    responseclima_o = requests.get(urlclima_o)
    #responseclima_d = requests.get(urlclima_d)
    clima_o = responseclima_o.json()
    #clima_d = responseclima_d.json()

    temperatura_origen = clima_o["current_condition"][0]["temp_C"]
    descripcion = clima_o["current_condition"][0]["lang_es"][0]["value"]
    return temperatura_origen, descripcion

def main(): 
    origen = input("ingrese una ciudad: ")
    temperatura_origen, descripcion = clima(origen)
    print(f"La temperatura actual de {origen} es de {temperatura_origen} °C. {descripcion}")

if __name__ == "__main__":
    main()