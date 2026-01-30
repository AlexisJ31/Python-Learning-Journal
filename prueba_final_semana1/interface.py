#crear un menu de opciones para el usuario
def mostrar_menu():
    #usaremos while para que el menu se muestre hasta que el usuario decida salir
    while True:
        print("Menu de opciones:")
        print("1. Ver jugadores")
        print("2. Agregar jugador")
        print("3. Salir")
        opcion = input("Seleccione una opcion (1-3): ")
        if opcion == "1":
            from conexion_bd import ver_jugadores
            ver_jugadores()
        elif opcion == "2":
            from conexion_bd import agregar_jugador
            from copia import ruta_origen
            nombre = input("Ingrese el nombre del jugador: ")
            posicion = input("Ingrese la posicion del jugador: ")
            dorsal = int(input("Ingrese el dorsal del jugador: "))
            # para guardar en sqlite
            agregar_jugador(nombre, posicion, dorsal)
            # para guardar en el archivo de texto
            ruta_origen(nombre, posicion, dorsal)

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")

