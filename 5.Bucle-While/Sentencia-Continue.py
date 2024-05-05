#Ejemplo de continue
print("While con la sentencia continue\n")
contador = 0
while contador < 10:
    contador+= 1
    if contador == 5:
        continue
    print("Valor de contador es : ", contador)