#Ejercicio 1 simulador de piques al dia para carrera
piques_diarios = 0
meta_piques = 5
while piques_diarios < meta_piques:
    piques_diarios += 1
    print(f"Vamos por el pique número: {piques_diarios}, falta poco para la meta de {meta_piques} piques diarios")
print("¡Meta de piques diarios alcanzada!")

#variante para que el ciclo se detenga
piques = 0
meta = 10

print("Entrenamiento iniciado...")

while piques < meta:
    piques += 1
    print(f"Pique #{piques} completado.")
    
    # Simulamos una lesión en el pique 4
    if piques == 4:
        print("¡AY! Sentí un tirón. Parando por precaución...")
        break # Esto rompe el ciclo 'while' de inmediato

print("Fin de la jornada.")

#variante en python para el do-while de java
# Imitando el "do-while" de Java
while True:
    print("--- Menú de Entrenamiento ---")
    print("1. Realizar pique")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")
    
    # Aquí es donde "preguntas" al final para ver si sigues o no
    if opcion == "2":
        print("Saliendo del programa...")
        break  # Este break es el que rompe el 'while True'
