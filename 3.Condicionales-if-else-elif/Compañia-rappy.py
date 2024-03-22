#Dias de vacaiones para cada departamento
print("SISTEMA DE DIAS DE VACACIONES")
name = input("¿Nombre del trabajador?: ")
service = int(input("¿Años de servicio?: "))
print("1.Atencion al cliente.\n2.Logistica\n3.Gerencia")
opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
   
    if service <= 1:
        print(f"El empleado -> {name} tiene 6 dias de vaciones")
    if service >1 and service <= 6:
        print(f"El empledao -> {name} tiene 14 dias de vacaciones")
    if service > 6:
        print(f"El empleado -> {name} tiene 20 dias de vacaciones")
elif opcion == 2:
    
    if service <= 1:
        print(f"El empleado de logistica -> {name} tiene 7 dias de vaciones")
    if service >1 and service <= 6:
        print(f"El empledao de logistica -> {name} tiene 15 dias de vacaciones")
    if service > 6:
        print(f"El empleado de logistica -> {name} tiene 22 dias de vacaciones")
elif opcion == 3:
   
    
    if service <= 1:
        print(f"El gerente -> {name} tiene 10 dias de vaciones")
    if service >1 and service <= 6:
        print(f"El gerente -> {name} tiene 20 dias de vacaciones")
    if service > 6:
        print(f"El gerente -> {name} tiene 30 dias de vacaciones")