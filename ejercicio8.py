"""
ejecicio 8:
un vendedor recibe un sueldo base un 10% extra por comision de su 
venta , el vendedor desea saber cuanto dinero obtendra por 
concepto de comisiones por las tres ventas que requiere en el mes  y en total que 
recibira en el mes tomando en cuenta su sueldo base y comision 
entrada:
venta 
comision
salidad: 
sueldo total
"""
venta1 = input("ingresar el total de la primer venta:")
venta1 = int(venta1)
venta2 = input("ingresar el total de la segundo venta:")
venta2 = int(venta2)
venta3= input("ingresar el total de la tercera venta:")
venta3 = int(venta3)
sueldo = int(venta3)
ventatotal = venta1 + venta2 +venta3
comision = ventatotal * 0.1
sueldototal = sueldo + comision
print("el sueldo total es de:",sueldototal)
