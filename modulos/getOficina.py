import storage.oficina as of
from tabulate import tabulate
#1.listado del codigo de oficinas y ciudad donde hay oficinas
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
          "codigo":val.get("codigo_oficiona"),
          "ciudad":val.get("ciudad")
        })
    return codigoCiudad

#2.listado con la ciudad y el telefono de las oficinas de españa

def getAllCiudadTelefono(pais):
    ciudadTelefono =[]
    for val in of.oficina:
      if(val.get("pais")=="España"):
        ciudadTelefono.append(
          {
            "ciudad": val.get("España"),
            "telefono": val.get("telefono")
          }
        )
    return ciudadTelefono
  
  
def getAllOficinaCiudad(codigoOfi):
    oficinaC = list()
    for val in of.oficina:
      if (val.get('ciudad') == ciudad):
        oficinaC.append({
          "Codigo": val.get('codigo_oficina'),
          "Origen": f"({val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')})",
          "Telefono": val.get('telefono'),
          "Direcciones":  f"({val.get('linea_direccion1')} {val.get('linea_direccion2')})"
          
        })
    return oficinaC   
  
# def menu():
#   while True:
#     print(""" 
          
#                ___                       _                   _       
#               | _ \ ___  _ __  ___  _ _ | |_  ___  ___    __| | ___  
#               |   // -_)| '_ \/ _ \| '_||  _|/ -_)(_-<   / _` |/ -_) 
#               |_|_\\___|| .__/\___/|_|   \__|\___|/__/   \__,_|\___| 
#                         |_|                                          
#                             __  _      _                                    
#                       ___  / _|(_) __ (_) _ _   __ _                        
#                      / _ \|  _|| |/ _|| || ' \ / _` |                       
#                      \___/|_|  |_|\__||_||_||_|\__,_|   
                                                  
#   1.Obtener la oficina por el codigo y la ciudad  
#   2.Ingrese la ciudad y le daremos los telefonos encontrados
#   3.obtener la informacion completa de una oficina segun su codigo
#   0.salir
#           """)
#     opcion = int(input("\nSelecione una de las opciones : "))
#     if(opcion == 1):
#         print(tabulate(getAllCodigoCiudad(), headers="keys",tablefmt="github"))
#     elif(opcion == 2):
#         codigoOficina = int(input("Ingrese el codigo del cliente : "))
#         print(tabulate(getAllCiudadTelefono(codigoOficina), headers="keys",tablefmt="github"))
#     elif(opcion == 3): 
#         ciudad = float(input("Ingrese el codigo de la oficina: "))
#         print(tabulate(getAllOficinaCiudad(ciudad),headers= "keys", tablefmt="github"))
#     elif(opcion == 0):
#          break 