import storage.producto as pro
from tabulate import tabulate
 #devuelve un listado con los productos que pertenecen a la gama ornamentales
 #y que tien emas de 100 unidades en stock .El listado debera estar ordenado 
 # por su precio de venta, mostrando en primer lugar  los de mayor precio
 
 
def getAllStocksPriceGama():
    gama = list()
    for val in pro.producto:
        if val.get ("gama") == "Ornamentales" and ("cantidad_en_stock") >= 100:
                gama.append({
                    "Codigo": val.get('codigo_producto'),
                    "Nombre": val.get('nombre'),
                    "precios": val.get('precio_venta'),
                    "Stock": val.get('cantidad_en_stock'),
                    "Descripcion": val.get('descripcion'),
                    "Proveedor": val.get('proveedor'),
                    "Gama": val.get('gama'),
                    "Dimencion": val.get('dimensiones')       
                })
    gamaOrdenada = sorted(gama, key=lambda precio: precio["precios"], reverse=True)
    return gamaOrdenada


def menu():
    while True:
        print("""
              
              1. Productos ornamentales stock mayor a 100
              0. Regresar a menu principal
              
              """)
        opcion = int(input("Seleccione una opcion"))
        if opcion == 1:
            print(tabulate(getAllStocksPriceGama(), headers="keys", tablefmt="rounded_grid"))
        elif opcion == 0:
            break
            


     