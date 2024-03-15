import storage.pago as pa
from tabulate import tabulate

def getAllFormapagoTotal():
    pagoTotal = []
    for val in pa.pago:
        if val.get("forma_pago") in ["Efectivo", "Tarjeta", "Transferencia"]:
            pagoTotal.append({
                "Forma_pago": val.get("forma_pago"),
                "Total": val.get("total"),
                "codigo_cliente": val.get("codigo_cliente")
            })
    return pagoTotal


#devuelve in listado con todos los pagos que se realizaron en el año 2008 
# mediante paypal, ordene el resultado de mayor a menor


def getAllPagoPaypal():
    añoPago= "2008"
    fechaPago = []
    repetidos = {}
    for val in pa.pago:
        if val.get("fecha_pago").startswith(añoPago) and val.get("codigo_cliente") not in repetidos:
            repetidos[val.get("codigo_cliente")]=True
            fechaPago.append({
                "codigo": val.get("codigo_cliente"),
                "Fecha_pago": val.get("fecha_pago"),
                "Total": val.get("total")
        })
    return fechaPago

#8.listado con el codigo de cliente de aquellos clientes que realizaron algun pago en 2008, tenga en cuenta que debe 
# eliminar aquellos codigos de cliente que aparezcan repetidos
def getAllPagos():
    CodigoFecha = []
    codigosVistos = set() 
    for val in pa.pago:
        if("2008") in val.get("fecha_pago"):
            Codigo_cliente = val.get("codigo_cliente")
            if Codigo_cliente not in codigosVistos:
                CodigoFecha.append({
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha": val.get("fecha_pago"),
                    "total": val.get("total")
                })
                codigosVistos.add(Codigo_cliente)
    return CodigoFecha

#devuelve un listado con todas las formas de pago que aparecen en la lista pago .
# Tenga en cuenta  que no deben  aparecer formas de pago repetidas

def getAllFormasPago():
    formas_pago = set()  
    for pago in pa.pago:
        formas_pago.add(pago.get("forma_pago"))
    return list(formas_pago)

def menu():
  while True:
    print(""" 
 
 ____  _________  ____  ____  _____  _____   ____  _____   ____  ____  _________ 
/  __\/  __/  __\/  _ \/  __\/__ __\/  __/  /  _ \/  __/  /  __\/  _ \/  __/  _ \
|  \/||  \ |  \/|| / \||  \/|  / \  |  \    | | \||  \    |  \/|| / \|| |  | / \|
|    /|  /_|  __/| \_/||    /  | |  |  /_   | |_/||  /_   |  __/| |-||| |_// \_/|
\_/\_\\____\_/   \____/\_/\_\  \_/  \____\  \____/\____\  \_/   \_/ \|\____\____/
                                                                                 
 
                                    
                                    
                                1.Obtener el codigo , la forma de pago y el total
                                2.clientes que realizaron un pago en 2008
                                3.clientes que realizaron un pago en 2008 mediante paypal
                                4.Formas de pago
                                0.salir
          """)
    opcion = int(input("\nSelecione una de las opciones : "))
    
    if(opcion == 1):
        print(tabulate(getAllFormapagoTotal(), headers="keys", tablefmt="github"))
        
    elif(opcion == 2):
        print(tabulate(getAllPagos(), headers="keys",tablefmt="github"))
        
    elif(opcion == 3): 
        print(tabulate(getAllPagoPaypal(),headers= "keys", tablefmt="github"))
        
    if(opcion == 4):
        print(tabulate(getAllFormasPago(), headers="keys", tablefmt="github"))
        
    elif(opcion == 0):
         break 