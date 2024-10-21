"""
ejercicio11:
pide el usuario de dos numeros y muestra la "distancia" entre ellos 
(el valor absoluto de su diferencia ,de modo que el resultado sea siempre positivo.)
entrada:
numero1:int
numero2:int
salida:
distacia
"""
num1 = input("intresa el numero:")
num1 = int(num1)
num2 = input("ingresa el segundo numero:")
num2 = int(num2)
distacia =num1 - num2
x = abs(distacia)
print("la distancia es de:" , x)