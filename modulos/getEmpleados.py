import storage.empleado as em
from tabulate import tabulate

#3.listado con nombre apellido y email de empleados cuyo jefe tiene un codigo de jefe igual a 7
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail =[]
    for val in em.empleados:
        if(val.get("codigo_jefe")== codigo):
            nombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')}{val.get('apellido2')}",
                    "email": val.get("email"),
                    "codigo" : val.get("codigo_jefe"),
                    "jefe":val.get("codigo_jefe")       
                }
            )
    return nombreApellidoEmail

#5.listado con el nombre apellidos y puesto de aquellos empleados que no sean representantes de ventas

def getAllNombreApellidoPuestoEmail():
    nombreApellPuestoEmail =[]
    for val in em.empleados:
        if (val.get("puesto"))!="Representante Ventas":
            nombreApellPuestoEmail.append(
            {
                    "nombre": val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')}{val.get('apellido2')}",
                    "puesto": val.get("puesto") 
            }
        )
    return nombreApellPuestoEmail

#4.devuelve el nombre, apellidos puesto email, del jefe de la empresa

def getAllNombreApellidosPuestoEmailJefeEmpresa(codigo):
    nomApePuestoEmailJefe =[]
    for val in em.empleados:
        if (val.get("codigo_jefe"))== codigo:
            nomApePuestoEmailJefe.append(
                {
                        "nombre": val.get("nombre"),
                        "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                        "email": val.get("email"),
                        "jefe": val.get("codigo_jefe"),
                        "puesto": val.get("puesto")
                }
            )
    return nomApePuestoEmailJefe
        
def menu():
  while True:
    print(""" 
          
                         ___                   _            _                      _             _        
                        | _ \___ _ __  ___ _ _| |_ ___   __| |___   ___ _ __  _ __| |___ __ _ __| |___ ___
                        |   / -_) '_ \/ _ \ '_|  _/ -_) / _` / -_) / -_) '  \| '_ \ / -_) _` / _` / _ (_-<
                        |_|_\___| .__/\___/_|  \__\___| \__,_\___| \___|_|_|_| .__/_\___\__,_\__,_\___/__/
                                |_|                                          |_|                          

                            1.Obtener la informacion de los empleados
                            2.Obtener nombre y apellido de los empleados que no sean representantes en ventas
                            3.obtener informacion del jefe de la empresa
                            0. Salir
          
          """)
    opcion = int(input("\nSelecione una de las opciones : "))

    if(opcion == 1):
        codigoJefe = int(input("Ingrese el codigo del jefe: "))
        print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="github"))

    elif(opcion == 2):
        print(tabulate(getAllNombreApellidoPuestoEmail(), headers="keys",tablefmt="github"))

    elif(opcion == 3): 
        codigo = int(input("Ingrese el codigo del jefe: "))
        print(tabulate(getAllNombreApellidosPuestoEmailJefeEmpresa(codigo),headers= "keys", tablefmt="github"))
          
    elif(opcion == 0):
        break
    
    
