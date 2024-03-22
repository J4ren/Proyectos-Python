#calcular todas las operaciones basicas
print("CALCULADORA")
print("1.SUMA\n2.RESTA\n3.PRODUCTO\n4.DIVISION\n5.DIVISION ENTERA\n6,EXPONENTE\n7.MODULO O RESTO")
opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    numero = float(input("Ingrese el primer numero: "))
    numero += float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
elif opcion == 2:
    numero = float(input("Ingrese el primer numero: "))
    numero -= float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
elif opcion == 3:
    numero = float(input("Ingrese el primer numero: "))
    numero *= float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
elif opcion == 4:
    numero = float(input("Ingrese el primer numero: "))
    numero /= float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
elif opcion == 5:
    numero = float(input("Ingrese el primer numero: "))
    numero //= float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
elif opcion == 6:
    numero = float(input("Ingrese el primer numero: "))
    numero **= float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
elif opcion == 7:
    numero = float(input("Ingrese el primer numero: "))
    numero %= float(input("Ingrese el segundo numero: "))
    print(f"RESULTADO: {numero}")
else: 
    print("Opcion invalida")