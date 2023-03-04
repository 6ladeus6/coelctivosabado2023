controladora = 100
print("*****Emapanadas******")
print("*********************")
print("1. agregar sabor de empanadas")
print("2. Mostrar sabor de empanadas")
print("3. cambiar sabor de empanadas")
print("0. salir")

while(controladora != 0):
    controladora = int(input("n\Digita una opción: "))
    if(controladora == 1):
        sabor = input("Agregue el sabor: ")
    elif (controladora ==2):
        print("n\El sabor ingresado es: ", sabor)
    elif controladora == 3:
        print("n\El sabor a cambiar es ", sabor)
        cambio = input(" el nuevo sabor: ")
        sabor = cambio
        print("n\El nuevo sabor es ", sabor)
    else: print("Ingrese una opción valida!!!")

 