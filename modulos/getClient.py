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
# listado de codigo del cliente y el nombre 
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
def getAllClientesPais(pais):
    clientesPais = []
    for val in cli.clientes:
        if val.get("pais")== pais:
            clientesPais.append({
                    "nombre": val.get("nombre_cliente"),
                    "pais":val.get("pais"),
                    "ciudad": val.get("ciudad"),
                    "region": val.get("region")
            })
    return clientesPais

def getAllClientePais(limiteCredit, pais):
    creditCliente =list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('pais')== pais):
            creditCliente.append({
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
    return creditCliente

def menu():
  while True:
    print("""  
          
                            ___                   _            _          _ _         _          
                            | _ \___ _ __  ___ _ _| |_ ___   __| |___   __| (_)___ _ _| |_ ___ ___
                            |   / -_) '_ \/ _ \ '_|  _/ -_) / _` / -_) / _| | / -_) ' \  _/ -_|_-<
                            |_|_\___| .__/\___/_|  \__\___| \__,_\___| \__|_|_\___|_||_\__\___/__/
                                    |_|                                                           
                                                                     
                1.obtener los clientes con su codigo y nombres
                2.obtener un cliente por su  codigo
                3.obtener la informacion completa de un cliente segun su limite de credito y ciudad que pertenece (ejem:1500.0,Fuenlabrada)
                4.obtener el nombre de la ciudad y region segun el pais
                5. Obtener toda la informacion completa de un cliente segun su limite de credito y pais que pertenece (ejem: 1500.0, 'USA')
                0. salir
              
          """)
    opcion = int(input("\nSelecione una de las opciones : "))

    if(opcion == 1):
        print(tabulate(getAllClientName(), headers="keys",tablefmt="github"))

    elif(opcion == 2):
        codigoCliente = int(input("Ingrese el codigo del cliente : "))
        print(tabulate(getoneClientecodigo(codigoCliente), headers="keys", tablefmt="github"))

        
    elif(opcion == 3):
            limite = float(input("Ingresa el limite de credito de los clientes q deseas visualizar: "))
            ciudad = input("Ingresa el nombre de la ciudad q deseas filtrar los clientes: ") 
            print(tabulate(getAllClientCiudad(limite, ciudad), headers="keys", tablefmt="github"))
       
    elif(opcion == 4):
        codigoCliente = str(input("Ingrese el nombre del pais: "))
        print(tabulate(getAllClientesPais(codigoCliente), headers="keys", tablefmt="github"))

    elif(opcion == 5): 
        limite = float(input("Ingrese el limite de credito : "))
        ciudad = str(input("Ingrese el nombre del pais: "))
        print(tabulate(getAllClientePais(limite,ciudad),headers= "keys", tablefmt="github"))
        
    elif(opcion == 0):
         break