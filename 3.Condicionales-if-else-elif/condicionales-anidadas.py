#ejemplo de uso 

print("1.Convertir de numero a palabra")
print("2.Convertir de palabra a numero")
opcion = int(input("¿Cual es su opcion?"))

if opcion == 1:
    numero = int(input("Ingrese el numero a convertir a palabra: "))
    if numero == 1:
        print("El numero es 'UNO'")
    elif numero == 2:
        print("El numero es 'DOS'")
    elif numero == 3:
        print("El numero es 'TRES'")
    elif numero == 4:
        print("El numero es 'CUATRO'")
    elif numero == 5:
        print("El numero es 'CINCO'")
elif opcion == 2:
    palabra = input("Ingrese la palabra a convertir en numero: ")
    if palabra == 'uno':
        print("El numero es '1")
    elif palabra == 'dos':
        print("El numero es '2' ")
    elif palabra == 'tres':
        print("El numero es '3' ")
    elif palabra == 'cuatro':
        print("El numero es '4' ")
    elif palabra == 'cinco':
        print("El numero es '5' ")
