'''Desarrollar un programa que imprima en pantalla la sucesion de fibonacci desde el numero 0 hasta
el numero 1597, de manera horizontal'''
x = 0
a = 1
while x < 1958:
    print(x, end=" ")
    x,a = a , x
    x+= a