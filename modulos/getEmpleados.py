import storage.empleado as em

#3.listado con nombre apellido y email de empleados cuyo jefe tiene un codigo de jefe igual a 7
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail =[]
    for val in em.empleados:
        if(val.get("codigo-jefe")==7):
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

def getAllNombreApellidoPuestoEmail(puesto):
    nombreApellPuestoEmail =[]
    for val in em.empleados:
        if (val.get("puesto"))!="Representante Ventas":
            nombreApellPuestoEmail.append(
            {
                    "nombre": val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')}{val.get('apellido2')}",
                    "email": val.get("email"),
                    "puesto": val.get("puesto") 
            }
        )
    return nombreApellPuestoEmail

#4.devuelve el nombre, apellidos puesto email, del jefe de la empresa

def getAllNombreApellidosPuestoEmailJefeEmpresa():
    nomApePuestoEmailJefe =[]
    for val in em.empleados:
        if (val.get("codigo_jefe"))== 3 and (val.get("Director Oficina")):
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
        
# def menu():
#     print(""" 
          
          
#                 ___                   _               _     
#                 | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___ 
#                 |   / -_) '_ \/ _ \ '_|  _/ -_|_-< / _` / -_)
#                 |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___|
#                 ___ _ |_| _ __| |___ __ _ __| |___ ___     
#                 / -_) '  \| '_ \ / -_) _` / _` / _ (_-<     
#                 \___|_|_|_| .__/_\___\__,_\__,_\___/__/     
#                             |_|                               
                            
#                             1.Obtener todod los clientes(codigo,nombre)
#                             2.obtener los datos del empleado segun su extencion
#                             3.

          
#           """)
