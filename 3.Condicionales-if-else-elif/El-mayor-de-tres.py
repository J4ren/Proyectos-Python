#Mayor de 3 numeros

print("Determinar el mayor de tres numeros")
num_uno =  int(input("Ingrese un numero: "))
num_dos =  int(input("Ingrese un numero: "))
num_tres =  int(input("Ingrese un numero: "))

if num_uno > num_dos and num_uno > num_tres:
    print(f"El numero {num_uno} es el mayor de los tres -> {num_uno} > {num_dos,num_tres}")
elif num_dos > num_uno and num_dos > num_tres:
    print(f"El numero {num_dos} es el mnayor de los tres -> {num_dos} > {num_uno,num_tres}")
else:
    print(f"El numero {num_tres} es el mnayor de los tres -> {num_tres} > {num_uno,num_dos}")