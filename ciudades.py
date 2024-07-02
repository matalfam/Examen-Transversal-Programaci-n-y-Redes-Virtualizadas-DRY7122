from geopy.distance import geodesic

ciudades = {
    "Santiago": (-33.4489, -70.6693),
    "Buenos Aires": (-34.6037, -58.3816),
    # Agrega más ciudades según sea necesario
}

def obtener_duracion(distancia, velocidad):
    return distancia / velocidad

while True:
    origen = input("Ciudad de Origen: ").title()
    destino = input("Ciudad de Destino: ").title()
    if origen == "S" or destino == "S":
        break
    
    if origen in ciudades and destino in ciudades:
        distancia_km = geodesic(ciudades[origen], ciudades[destino]).kilometers
        distancia_mi = geodesic(ciudades[origen], ciudades[destino]).miles
        
        print(f"Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
        
        transporte = input("Seleccione el tipo de transporte (auto, avion, bicicleta): ")
        if transporte.lower() == "auto":
            velocidad = 100  # km/h
        elif transporte.lower() == "avion":
            velocidad = 800  # km/h
        elif transporte.lower() == "bicicleta":
            velocidad = 20  # km/h
        else:
            print("Transporte no válido. Selecciona auto, avion o bicicleta.")
            continue
        
        duracion = obtener_duracion(distancia_km, velocidad)
        print(f"Duración estimada en {transporte}: {duracion:.2f} horas")
        print(f"Viaje de {origen} a {destino} atravesando {distancia_km:.2f} km.")
    else:
        print("Una o ambas ciudades no están en la lista`.")
