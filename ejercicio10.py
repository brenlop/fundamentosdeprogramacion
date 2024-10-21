"""
ejecucio10:
un alumno desea saber su calificacion final en la materia 
de los algoritmos dicha calificacion secompone con los siguentes porcentajes 
55% del promedio de sus tres calificaciones paoraciales
30% de la calificacion del examen final
15% de la calificacion de un trabajo final 
entrada:
parcial final
examen final 
trabajo final 
salida:
calificacion final
"""
parcial1 = input("ingresa la calificacion del primer parcial:")
parcial1 = int(parcial1)
parcial2 = input("ingresa la aclificacion de la segundo parcial:")
parcial2 = int(parcial2)
parcial3 = input("ingresa la calificacion de la trecer pacial:")
parcial3 = int(parcial3)
examenfinal = input=("ingresa la calificacion de el examenfinal:")
examenfinal = int(examenfinal) 
trabfinal = input("ingresa la calificacion del trabajo final:")
trabfinal = int(examenfinal)
parciales = parcial1 + parcial2 + parcial3
promedio = parciales/3
calfinal  = promedio * 0.55 + examenfinal * 0.3 +trabfinal * 0.15
print("la calificacion final es" , calfinal)