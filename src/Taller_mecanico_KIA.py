BIENVENIDA="""
Bienvenido este es un programa que simula el inventario de vehiculos del area del mantenimiento
de una agencia de KIA motors
"""
MODELOS=""" Estos son los modelos que maneja la marca
Sedanes: Rio, K3, K4, Optima, Stinger 
SUVS: EV6, Sportage e-HYBRID, Sonet, Telluride, Seltos, Niro, Sorento, Carnival"""
DESPEDIDA="""Saliendo...
Gracias por usar este programa, este programa fue desarrollado por JulioGilzChang"""
ADVERTENCIA= """No se Agregó el vehiculo 
ya que no se encuentra en la lista de los modelos que te enseñamos en un principio,
o puede que hayas escrito el nombre mal, favor de escribirlo tal cual se muestra en la lista.
Intentelo de nuevo.
"""
vacio="""La lista de los vehiculos del área del mantenimiento está vacío 
agregue un modelo de vehiculo de la lista que se le mostró.
"""

inventario=[]

concesionario= ["Rio", "K3","K4", "Optima", "Stinger",
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
        while True:
            print("\ningresa el modelo que quieres agregar: " )
            modelo=input("Modelo ").strip()

            if modelo in concesionario:
                inventario.append(modelo)
                print(f" Modelo {modelo} agregado al inventario. ")
                break
            else:
                print(ADVERTENCIA)

    elif opcion == "2":
        
            print(" \nIngresa el modelo del vehiculo que quieres quitar de la lista: ")
            modelo = input(" modelo: ").strip()
            if not inventario:
                print(vacio)
            elif modelo in inventario:
                inventario.remove(modelo)
                print(f" Vehiculo {modelo} eliminado del inventario. ")
            else:
                print(f"El vehiculo {modelo} no se encuentra en la lista ")

    elif opcion == "3":
        if not inventario:
            print(vacio)
        else:
            print(" \n Inventario actualizado: ")
        print(inventario)

    elif opcion == "4":
        print(DESPEDIDA)
        break

    else:
        print("Opcion no valida. Por favor ingrese oun numero del 1 al 4")

