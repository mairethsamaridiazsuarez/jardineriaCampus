
#from tabulate import tabulate
#import sys
import modulos.getClient as cliente
import modulos.getOficina as oficina
import modulos.getEmpleados as empleado
import modulos.getProducto as producto
import modulos.getPedidos as pedido
import modulos.getPago as pago


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
            producto.menu() 
            
        elif opcion == 5:
            pedido.menu() 
            
        elif opcion == 6:
            pago.menu() 
        elif(opcion==0):
            break
  
        

