"""
ejecicico 9:
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuánto deberá pagar finalmente por su compra.
entrda:
cliente
salida:
total para pagar
"""
totalcompra = input("ingresar el totalde la compra:")
totalcompra = int(totalcompra)
descuento = totalcompra * 15
descuento = descuento / 100
total = totalcompra - descuento
print ("el total a pagar aplicando el descuento es:", total)