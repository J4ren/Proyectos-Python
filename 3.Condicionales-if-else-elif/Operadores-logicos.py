#Ejemplo de uso de AND -> ambas condiciones deben ser ciertas
numero = 5
numero_2 = 5
if numero == 5 and numero_2 >= 5:
    print("AMBAS CONDICIONES SE HAN CUMPLIDO")
else:
    print("UNO O AMBAS CONDICIONES NO SE CUMPLEN")

#Ejemplo de uso de OR -> uno o ambas condiciones deben ser ciertas
numero = 5
numero_2 = 2
if numero == 5 and numero_2 >= 5:
    print("UNO O AMBAS CONDICIONES SE HAN CUMPLIDO")
else:
    print("NUNGUNA DE LAS CONDICIONES SE CUMPLEN")
#Ejemplo de uso del not -> lo que hace es negar la condicion

numero_2 = 2
if not numero_2 > 5:
    print("La condicion se invirtio y se cumple al ser un numero  menor o igual a 5")
else:
    print("No se cumple la condicion porque es mayor a 5")
