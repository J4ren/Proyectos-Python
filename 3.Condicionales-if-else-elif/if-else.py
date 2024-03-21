'''sintaxis
if condicion:
    instrucciones
else: 
    instrucciones'''
#Ejemplo de uso 
numero = 5 
if numero == 5:
    print("El numero es cinco")
else:
    print("El numero no es cinco")

#Otro ejemplo: 
print("Sistema para calcular promedio de alumnos")
nombre = input("¿Cual es tu nombre?: ")

fisica = float(input("Nota en Fisica: "))
lp = float(input("Nota en Lenguaje de programacion 2: "))
administracion = float(input("Nota de administracion General: "))
bdd = float(input("Nota de base de datos 2: "))
ingles = float(input("Nota de ingles tecnico 1: "))
promedio = (fisica + lp + administracion + bdd + ingles)/5

if promedio >10:
    print(f"Felicitaciones {nombre} usted a aprobado el semestres, Promedio Final: {promedio}.")
else:
    print(f"Desaprobado, promedio {promedio}")
    