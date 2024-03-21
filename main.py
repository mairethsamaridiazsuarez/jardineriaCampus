
#from tabulate import tabulate
#import sys
import os
import modulos.getClient as cliente
import modulos.getOficina as oficina
import modulos.getEmpleados as empleado
import modulos.getProducto as producto
import modulos.getPedidos as pedido
import modulos.getPago as pago
import modulos.getProducto as Repproducto
import modulos.postProducto as CRUDproducto


def menuProducto():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/ __\__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____                                
 / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                
/ /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                 
\__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                                  
            /_/                                                                                  
        
            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal
          
            """)
        opcion = int(input("\nSelecciona una de las opciones: "))
        if(opcion == 1):
            Repproducto.menu()
        if(opcion == 2):
            CRUDproducto.menu()
        if(opcion == 0):
            break
            



if(__name__== "__main__"):
    while True:
        print(""" 
                                         __  __                   ___       _            _              _ 
                                        |  \/  | ___  _ _  _  _  | _ \ _ _ (_) _ _   __ (_) _ __  __ _ | |
                                        | |\/| |/ -_)| ' \| || | |  _/| '_|| || ' \ / _|| || '_ \/ _` || |
                                        |_|  |_|\___||_||_|\_,_| |_|  |_|  |_||_||_|\__||_|| .__/\__,_||_|
                                                                                            |_|
                                                                
                                                                1. cliente
                                                                2. oficina   
                                                                3. empleados
                                                                4. producto 
                                                                5. pedido 
                                                                6. pago
                                                                0. salir                                                       
""" )
        opcion = int(input("\n seleccione una de las opciones: "))
        
        if(opcion== 1):
            cliente.menu()
            
        elif(opcion==2):
            oficina.menu()
            
        elif(opcion==3):
            empleado.menu()  
            
        elif opcion == 4:
            menuProducto() 
            
        elif opcion == 5:
            pedido.menu() 
            
        elif opcion == 6:
            pago.menu() 
        elif(opcion==0):
            break
  
        

