saludo = "Hola"
saludo += " "
saludo += "jaren"

print(saludo)

#convirtiendo un numero entero a string 

numero_1 = 3
numero_2 = 4
#conversion
resultado = str(numero_1 + numero_2)
print ("El resultado es: " + resultado)

#busqueda de strings 
mensaje = "hola jaren"
sub_cadena = mensaje.find("jaren")
#nos arroja un numero entero de la posicion
print(sub_cadena)

#Extraccion
mensaje = "Hola Ernesto"
extraccion = mensaje[1:8]
print(extraccion)

#comparacion 
mensaje = "Hola"
mensaje_2 = "Hola"

print(mensaje == mensaje_2)