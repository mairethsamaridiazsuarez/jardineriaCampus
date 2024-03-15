import storage.oficina as of
from tabulate import tabulate

#1.listado del codigo de oficinas y ciudad donde hay oficinas
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
          "codigo":val.get("codigo_oficina"),
          "ciudad":val.get("ciudad")
        })
    return codigoCiudad


#2.listado con la ciudad y el telefono de las oficinas  segun el pais
def getAllCiudadTelefono(pais):
    ciudadTelefono =[]
    for val in of.oficina:
      if(val.get("pais")== pais):
        ciudadTelefono.append(
          {
            "ciudad": val.get("ciudad"),
            "telefono": val.get("telefono")
          }
        )
    return ciudadTelefono
 
  
  # listado con  el codigo , origen ,telefono y direcciones ,segun la ciudad
def getAllOficinaCiudad(ciudad):
    oficinaC = list()
    for val in of.oficina:
      if (val.get("ciudad") == ciudad):
        oficinaC.append({
          "Codigo": val.get('codigo_oficina'),
          "Origen": f"({val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')})",
          "Telefono": val.get('telefono'),
          "Direcciones":  f"({val.get('linea_direccion1')} {val.get('linea_direccion2')})"
          
        })
    return oficinaC   
 
  
def menu():
  while True:
    print(""" 
          
                             ___                   _            _            __ _    _           
                            | _ \___ _ __  ___ _ _| |_ ___   __| |___   ___ / _(_)__(_)_ _  __ _ 
                            |   / -_) '_ \/ _ \ '_|  _/ -_) / _` / -_) / _ \  _| / _| | ' \/ _` |
                            |_|_\___| .__/\___/_|  \__\___| \__,_\___| \___/_| |_\__|_|_||_\__,_|
                                    |_|                                                         
                                                                                      
                                  1.Obtener el codigo de oficina y la ciudad  donde se encuentran
                                  2.Obtener la ciudad y el telefono de las oficinas de un pais
                                  3.obtener el codigo ,telefono y direccion segun la ciudad
                                  0.salir
          """)

    opcion = int(input("\nSelecione una de las opciones : "))

    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))

    elif(opcion == 2):
        pais = str(input("Ingrese el pais : "))
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))

    elif(opcion == 3): 
        ciudad = str(input("Ingrese la ciudad: "))
        print(tabulate(getAllOficinaCiudad(ciudad), headers="keys", tablefmt="github"))

    elif(opcion == 0):
         break 


