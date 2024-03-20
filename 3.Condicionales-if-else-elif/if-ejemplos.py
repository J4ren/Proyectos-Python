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