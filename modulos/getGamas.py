import json
import requests

def getAllGama():
    #json-server storage/producto.json -b 5002
    peticion = requests.get("http://192.168.253.128:5002")
    data = peticion.json()
    return data
def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
    