BIENVENIDA="""
Bienvenido este es un programa que simula el inventario de vehiculos del area del mantenimiento
de una agencia de KIA motors
"""
MODELOS=""" Estos son los modelos que maneja la marca
Sedanes: Rio, K3, K4, Optima, Stinger 
SUVS: EV6, Sportage e-HYBRID, Sonet, Telluride, Seltos, Niro, Sorento, Carnival"""
DESPEDIDA="""Saliendo...
Gracias por usar este programa, este programa fue desarrollado por JulioGilzChang"""

inventario= ["Rio", "K3","K4", "Optima", "Stinger",
"EV6", "Sportage e-HYBRID", "Sonet" , "Telluride", "Seltos", "Niro" ,"Sorento", "Carnival"]

OPCIONES="""
Opciones:
1)Agregar un vehiculo
2)Quitar un vehiculo
3)Mostrar inventario actualizado
4)salir 

"""
print(BIENVENIDA)
print(MODELOS)

while True: 
    print(OPCIONES)
    opcion=input(" Elige una opcion del (1 al 4): ")

    if opcion == "1":
        print("\ningresa el modelo que quieres agregar: " )
        modelo=input("Modelo ").strip()

        if modelo:
            inventario.append(modelo)
            print(f" Modelo {modelo} agregado al inventario. ")
        else:
            print(" Modelo no válido. No se agregó el vehiculo ")

    elif opcion == "2":
        print(" \nIngresa el modelo del vehiculo que quieres quitar de la lista: ")
        modelo = input(" modelo: ").strip()

        if modelo in inventario:
            inventario.remove(modelo)
            print(f" Vehiculo {modelo} eliminado del inventario. ")
        else:
            print("El vehiculo {modelo} no se encuentra en la lista ")

    elif opcion == "3":
        print(" \n Inventario actualizado: ")
        print(inventario)

    elif opcion == "4":
        print(DESPEDIDA)
        break

    else:
        print("Opcion no valida. Por favor ingrese oun numero del 1 al 4")

