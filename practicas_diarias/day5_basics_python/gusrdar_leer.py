import os
# imprimir la bienvenida a la convocatoria del equipo
print("¡Bienvenidos a la convocatoria del equipo!")
# usaremos try except para manejar errores al abrir el archivo
try:
    # leer que jugador desea convocar
    jugador = input("Ingrese el nombre del jugador que desea convocar: ")
    # Guardar (Modo 'a' de Append para no borrar a los anteriores)
    with open("convocados.txt", "a") as archivo:
        archivo.write(jugador + "\n")

    #im0primimos si el jugador se gusrdo correctamente
    print(f"El jugador {jugador} ha sido convocado correctamente.")

    # Leer el archivo para mostrar la lista de convocados
    print("\nLista de jugadores convocados:")
    with open("convocados.txt", "r") as archivo:
        #aqui leemos todas las lineas del archivo
        convocados = archivo.readlines()
        #preguntamos si hay convocados
        if convocados:
            for jugador in convocados:
                print(jugador.strip())  # Usamos strip() para eliminar saltos de línea
        else:
            print("No hay jugadores convocados aún.")
except Exception as e:
    print(f"Ocurrió un error: {e}")