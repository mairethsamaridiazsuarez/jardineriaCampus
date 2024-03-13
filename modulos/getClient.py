import storage.cliente as cli
from tabulate import tabulate

def getAllClientName():
    clienteName = list()
    for val in cli.clientes:
        codigoName = dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get("nombre_cliente")
        })
        clienteName.append(codigoName)
    return clienteName

def getoneClientecodigo(codigo):
    codigoCliente = list()
    for val in cli.clientes:
        if(val.get('codigo_cliente')==codigo):
            codigoCliente.append({    
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
    return codigoCliente
        
        
def getAllClientCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad')== ciudad):
           clienteCredic.append({
                "Codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": f"{val.get('nombre_contacto')} {val.get('nombre_contacto')}",
                "Telefono": val.get('telefono'),
                "Fax": val.get('fax'),
                "Direcciones": f"({val.get('linea_direccion1')} {val.get('linea_direccion2')})",
                "Origen": f"({val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')})",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": val.get('limite_credito')               
        })           
    return clienteCredic
#6. listado con el nombre de todos los clientes españoles
def getAllClientesEspañol():
    clientesEspañol = []
    for val in cli.clientes:
        if val.get("pais")=="spain":
            clientesEspañol.append({
                    "nombre": val.get("nombre_cliente"),
                    "pais":val.get("pais"),
                    "ciudad": val.get("ciudad"),
                    "region": val.get("region")
            })
    return clientesEspañol

# def menu():
#     print("""
          
#                         _               _       _             _ _         _          
#   _ _ ___ _ __  ___ _ _| |_ ___ ___  __| |___  | |___ ___  __| (_)___ _ _| |_ ___ ___
#  | '_/ -_) '_ \/ _ \ '_|  _/ -_|_-< / _` / -_) | / _ (_-< / _| | / -_) ' \  _/ -_|_-<
#  |_| \___| .__/\___/_|  \__\___/__/ \__,_\___| |_\___/__/ \__|_|_\___|_||_\__\___/__/
#          |_|                                                                         
# 1.obtener todos los clientes (codigo y nombre)
# 2. obtener un cliente por el codigo
# 3. obtener la informacion completa de un cliente segun su limite de credito y ciudad que pertenece (ejem:1500.0,Fuenlabrada)
              
#           """)
#     opcion = int(input("\nSelecione una de las opciones : "))
#     if(opcion == 1):
#         print(tabulate(getAllClientName(), headers="keys",tablefmt="github"))
#     elif(opcion == 2):
#         codigoCliente = int(input("Ingrese el codigo del cliente : "))
#         print(tabulate(getoneClientecodigo(codigoCliente), headers="keys",tablefmt="github"))
#     elif(opcion == 3): 
#         limite = float(input("Ingrese el limite de credito de los clientes que deseas visualizar : "))
#         ciudad = input("Ingrese el nombre de la ciudad que deseas filtrar los clientes : ")
#         print(tabulate(getAllClientCiudad(limite,ciudad),headers= "keys", tablefmt="github"))