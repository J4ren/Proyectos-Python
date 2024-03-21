print("Introduce dos numeros a comparar")

num_uno = int(input("Ingrese el primer numero: "))
num_dos = int(input("Ingrese el segundo numero: "))

print(f"Los numeros a comparar son {num_uno} y {num_dos}")

if num_uno == num_dos:
    print("ES IGUAL...")
if num_uno != num_dos:
    print("ES DIFERENTE...")
if num_uno < num_dos:
    print("ES MENOR...")
if num_uno > num_dos:
    print("ES MAYOR...")
if num_uno <= num_dos:
    print("ES MENOR O IGUAL...")
if num_uno >= num_dos:
    print("ES MAYOR O IGUAL...")