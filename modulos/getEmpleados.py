import storage.empleado as em

#listado con nombre apeelido y email cuyo codigo de jefe es siete
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail =[]
    for val in em.empleados:
        if(val.get("codigo-jefe")==codigo):
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

def getAllNombreApellidoPuestoEmail(puesto):
    NombreApellidoPuestoEmail =[]
    for val in em.empleados:
        if (val.get("puesto"))!="Representante Ventas":
            NombreApellidoPuestoEmail.append(
            {
                    "nombre": val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')}{val.get('apellido2')}",
                    "email": val.get("email"),
                    "puesto": val.get("puesto") 
            }
        )
    return NombreApellidoPuestoEmail

#devuelve el nombre, apellidos puesto email, del jefe de la empresa

def getAllNombreApellidosPuestoEmailJefeEmpresa():
    nombreApellidosPuestoEmailJefeEmpresa =[]
    for val in em.empleados:
        if (val.get("codigo_jefe"))== 3 and (val.get("Director Oficina")):
            nombreApellidosPuestoEmailJefeEmpresa.append(
                {
                        "nombre": val.get("nombre"),
                        "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                        "email": val.get("email"),
                        "jefe": val.get("codigo_jefe"),
                        "puesto": val.get("puesto")
                }
            )
    return nombreApellidosPuestoEmailJefeEmpresa
        
