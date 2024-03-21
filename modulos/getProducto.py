from tabulate import tabulate
#import json
import os
import requests
import modulos.postProducto as  psProducto

 #devuelve un listado con los productos que pertenecen a la gama ornamentales y que tien emas de 100 unidades en stock .El listado debera estar ordenado por su precio de venta, mostrando en primer lugar  los de mayor precio

#json-server storage/producto.json -b 5001

def getAllData():
    peticion = requests.get("http://192.168.253.128:5001")
    data = peticion.json()
    print(data[0])
    
def getAllStocksPriceGama(gama , stock):
    condiciones = []
    for val in getAllData():
        if (val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {       
                "Codigo": val.get("codigo_producto"),
                "venta": val.get("precio-venta"),
                "Nombre": val.get("nombre"),
                "Gama": val.get("gama"),
                "Dimencion": val.get("dimensiones"),
                "Proveedor": val.get("proveedor"), 
                "Descripcion": f'{val.get("descripcion")[:5]}...' if condiciones [i].get("descripcion") else None,
                "Stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")         
            }
    return condiciones

def menu():
    while True:
        os.system("clear")
        print("""
                      

                     ___                   _            _                        _         _       
                    | _ \___ _ __  ___ _ _| |_ ___   __| |___   _ __ _ _ ___  __| |_  _ __| |_ ___ 
                    |   / -_) '_ \/ _ \ '_|  _/ -_) / _` / -_) | '_ \ '_/ _ \/ _` | || / _|  _/ _ \
                    |_|_\___| .__/\___/_|  \__\___| \__,_\___| | .__/_| \___/\__,_|\_,_\__|\__\___/
                            |_|                                |_|                                 


    1. Obtener todos los productos de una categoría ordenando sus precios de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100 )
    0. Salir                              
              """)
        opcion = int(input("Seleccione una opcion : "))
        
        if(opcion == 1):
            tipoGama = input("Ingrese la gama que deseas filtrar: ")
            stock = int(input("Ingrese las unidades que deceas mostrar : "))
            print(tabulate(getAllStocksPriceGama(tipoGama, stock), headers="keys", tablefmt="github"))
        elif(opcion == 0):
            break 

