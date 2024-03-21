import json
import os
import requests
from tabulate import tabulate
import modulos.getGamas as gG
import modulos.postProducto as  psProducto

def postProducto():
    #json-server storage/producto.json -b 5001
    
    productolista = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidadEnStock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    }

    peticion = requests.post("http://192.168.253.128:5001/productos", data = json.dumps(productolista))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print("""
                      
    ___       __          _       _      __                         __      __                    __        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/      
    ____  ____  ____  ____  __  __________________  _____                                                   
   / __ \/ __ \/ __ \/ __ \/ / / / ____/_  __/ __ \/ ___/                                                   
  / /_/ / /_/ / / / / / / / / / / /     / / / / / /\__ \                                                    
 / ____/ _, _/ /_/ / /_/ / /_/ / /___  / / / /_/ /___/ /                                                    
/_/   /_/ |_|\____/_____/\____/\____/ /_/  \____//____/     

                                        
                                        1. Guardar un producto nuevo
                                        0. Salir
                                        
              """)
        opcion = int(input("Seleccione una opcion : "))
        
        if(opcion == 1):
            print(tabulate(postProducto(), headers="keys", tablefmt="github"))
   
          
        elif(opcion == 0):
            break 
        
        input("Precione una tecla para continuar.....")



