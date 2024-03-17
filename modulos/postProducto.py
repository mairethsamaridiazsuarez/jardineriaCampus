import json
import requests
def postProducto(producto):
    #json-server storage/producto.json -b 5001
    peticion = requests.post("http://192.168.253.128:5001", data = json.dumps(producto ))
    res = peticion.json()
    return res


