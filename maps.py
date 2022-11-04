import requests 
import urllib


api_url = "http://www.mapquestapi.com/directions/v2/route?"
#el signo de interrogacion significa que vamos a separar la parte de la url con los recursos

#Llave para acceder a mapquest
key = "VUMTeSQl2G6JzINKnAuas25bl9dfkzAk"

#Creacion de la url
#url = api_url + urllib.parse.urlencode({"key":key, "from": origin, "to":destination}) 
#parse.urlencode va a codificar el diccionario que acabamos de crear dentro de la url de arriba

#creamos un formato json para leer los datos que obtenemos apartir de la url
#json_data = requests.get(url).json()
#print(json_data), con esto podemos observar un "diccionario" de sitio sugeridos o rutas mas comunes 
# que nos guiaran al destino 

while True:
#creamos las variables de punto de partida y el destino 
    origen = input("Ingresa el punto de partida de tu viaje: ")
    if origen == "q":
        break
    destino = input("¿Hacia donde te diriges?: ")
    if destino == "q":
        break
    
    url = api_url + urllib.parse.urlencode({"key":key, "from": origen, "to":destino}) 
    json_data = requests.get(url).json()
    statuscode = json_data["info"]["statuscode"] 

#creamos el codigo para que se visualice el clima de la ciudad de origen y la de destino 
def main():
    urlclima = f"https://es.wttr.in/{origen}?format=j1"

    responseclima = requests.get(url)
    clima = responseclima.json()

    temperatura_origen = clima["current_condition"][0]["temp_C"]
    descripcion = clima["current_condition"][0]["lang_es"][0]["value"]
    print(f"La temperatura actual de {origen} es de {temperatura_origen} °C. {descripcion}")

if __name__ == "__main__":
    main()

#creamos un if para cuando sea exitosa la ejecucion y creamos variables de interes a resaltar del json   

    if statuscode == 0:
        duracion_del_viaje = json_data["route"]["formattedTime"]
        distancia = json_data["route"]["distance"] * 1.61
        #gasolina_usada = json_data["route"]["fuelUsed"] * 3.79
        #velocidad_promedio = str(distancia/duracion_del_viaje)
        print("============================================================")
        print(f"informacion del viaje desde {origen.capitalize()} hasta {destino.capitalize()}:")
        print(f"La duracion de su trayecto en coche fue: {duracion_del_viaje}.")
        print("La distancia aproximada del viaje fue de:  " + str("{:.2f}".format(distancia) + "km."))
        #print(f"la velocidad promedio fue de {velocidad_promedio} km/h.")
        #print("Usaste :  " + str("{:.2f}".format(gasolina_usada) + "litros de gasolina en tu viaje."))
        print(url)
        
        print("============================================================")
        print("Indicaciones del trayecto")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"])








