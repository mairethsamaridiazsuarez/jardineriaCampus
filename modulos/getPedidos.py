import storage.pedido as pe
from datetime import datetime
#7. listado con los distintos estados que puede pasar un pedido
def getAllEstadosDePedido():
    estadoPedido = []
    for val in pe.pedido:
        estadoPedido.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado_pedido":val.get("estado"),
            "comentario": val.get("comentario")
        })      
    return estadoPedido

#9.listado con el codigo de pedido , codigo de cliente, fecha esperada y 
# fecha de entrega de los pedidos que no han sido entregados a tiempo

def getAllCodigoEsperadaEntregaPedido():
    estadoPedidoCodigo = []
    for val in pe.pedido:
        if val.get("estado")=="Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start= datetime.strptime(date_2, "%d/%m/%Y")
            end = datetime.strptime(date_1, "%d/%m/%Y")
            diff = end.date() - start.date()              
            if(diff.days <0):
                estadoPedidoCodigo.append({
                "codigo_pedido": val.get("codigo_pedido"),
                "estado_pedido":val.get("estado"),
                "fecha_entrega":val.get("fecha_entrega"),
                "comentario": val.get("comentario")

                                        })
        
    return estadoPedidoCodigo


#10.listado con el codigo de pedido ,codigo de cliente, fecha esperada y fecha entrega de
# los  pedidos cuya fecha de entrega ha sido al menos dos dias antes de la fehca esperada

def getAllCodiPediMen2():
    listadoPedidos = []
    for pedido in pe.pedido:
        if pedido.get("estado") == "Entregado" and pedido.get("fecha_entrega") is not None:
            fecha_entrega = datetime.strptime(pedido.get("fecha_entrega"), "%Y-%m-%d")
            fecha_esperada = datetime.strptime(pedido.get("fecha_esperada"), "%Y-%m-%d")
            if (fecha_esperada - fecha_entrega).days >= 2:
                listadoPedidos.append({
                    "codigo_pedido": pedido.get("codigo_pedido"),
                    "codigo_cliente": pedido.get("codigo_cliente"),
                    "fecha_esperada": pedido.get("fecha_esperada"),
                    "fecha_entrega": pedido.get("fecha_entrega")
                })
        
    return listadoPedidos

#11.listado de todos los pedidos rechazados en 2009

