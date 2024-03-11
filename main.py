
from tabulate import tabulate
import modulos.getClient as cliente
import modulos.getOficina as oficina
import modulos.getEmpleados as empleado

def menu():
    print(""" 

  __  __                   ___       _            _              _ 
 |  \/  | ___  _ _  _  _  | _ \ _ _ (_) _ _   __ (_) _ __  __ _ | |
 | |\/| |/ -_)| ' \| || | |  _/| '_|| || ' \ / _|| || '_ \/ _` || |
 |_|  |_|\___||_||_|\_,_| |_|  |_|  |_||_||_|\__||_|| .__/\__,_||_|
                                                    |_|
                                                    
    1. cliente
    2. oficina   
    3. empleados
    4. pedidos                                                         
""" )
    opcion = int(input("\n seleccione una de las opciones: "))
    if(opcion== 1):
        cliente.menu()
    elif(opcion==2):
        oficina.menu()
    elif(opcion==3):
        empleado.menu()   
menu()