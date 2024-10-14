"""
ejercicio 3:
programa que calcula la hipotenusa de un triangulo
rectangulo a partir de sus catetos 
entrada:
cateto1: int
cateto2: int
salidas:
hipotenusa
analisis:
se resuelve con el teorema de pitagoras
"""
import math 
cateto1 = input("escribe el cateto 1:")
cateto2 = int(cateto1)
cateto1 = int(input("escribe el cateto 2: "))
hipotenusa = cateto1 * cateto1+ cateto2 * cateto2
hipotenusa = hipotenusa ** (1/2)
print ("La hipotenusa es:", hipotenusa)
