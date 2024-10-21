"""
ejercicio12:
pide al usuario  dos pares de numeros x1,y2 y x2,y2, que representa
dos numeros puntos del plano. calcular y muestra la distancia entre ellos.
entrada:
num1x:int
num1y:int
num2x:int
num2y:int
salida:
distancia
"""
num1x = input("ingresa el primer numero x:")
num1x =int(num1x)
num1y = input("ingresa el primer numero y:")
num1y = int(num1y)
num2x = input("ingresa el segundo numero x:")
num2x = int(num2x)
num2y = input("ingresa el segundo numero y:")
num2y = int(num2y)
distacia = num1x +num1y * num1x +num1y + num2x +num2y *num2x +num2y
resultado = distacia ** (1/2)
print("la distancia es de:" , resultado)
