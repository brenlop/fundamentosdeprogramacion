"""
ejercicio14:
un numero de dos cifrass ,diseñe un algoritmo que permite obtener el 
numero invertido
entrada:
numeros 
salida:
numero invertido
"""
num = input("ingresa un numero de dos cifras:")
num = int(num)
dec = num // 10
uni = % 10 
print("el numero invertido es:", uni ,dec)