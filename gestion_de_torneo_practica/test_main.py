import sqlite3
import os
# IMPORTANTE: Aquí traemos las funciones de tus otros archivos
# Asegúrate de que los archivos se llamen exactamente así (sin el .py)
from base_de_datos import crear_tabla, crear_tabla_marcadores, ver_marcadores, agregar_jugador, ver_jugadores
from filtrar_jugador import filtrar_jugador_por_posicion
from filtrar_fecha import validar_fecha_domingo

    # 1. Preparamos la casa
crear_tabla()
crear_tabla_marcadores()
    
while True:
        print("\n⚽ SISTEMA DE TORNEO - UTP ⚽")
        print("1. Registrar nuevo jugador")
        print("2. Ver todos los jugadores")
        print("3. Buscar por posición (ej. Contención)")
        print("4. Validar día de juego")
        print("5. Ver marcadores")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            nom = input("Nombre: ")
            pos = input("Posición: ")
            edad = int(input("Edad: "))
            # Pasamos '1' para True o '0' para False porque es SQLite
            eq = 1 if input("¿Tiene equipo? (s/n): ").lower() == 's' else 0
            agregar_jugador(nom, pos, edad, eq)
            
        elif opcion == "2":
            ver_jugadores()
            
        elif opcion == "3":
            pos_busqueda = input("Ingresa posición a filtrar: ")
            filtrar_jugador_por_posicion(pos_busqueda)
            
        elif opcion == "4":
            dia_input = input("Ingresa el día actual: ")
            if validar_fecha_domingo(dia_input):
                print("✅ ¡Hoy es Domingo de fútbol! A jugar.")
            else:
                print("❌ Hoy no hay liga. Solo se juega los Domingos.")
                
        elif opcion == "5":
            ver_marcadores()
            
        elif opcion == "6":
            print("¡Nos vemos en la cancha, Aimar!")
            break
        else:
            print("Opción inválida.")
