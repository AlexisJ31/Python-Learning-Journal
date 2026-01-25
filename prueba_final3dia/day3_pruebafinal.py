#prueba 1
#definimos una lista de ejercicios
ejercicios = ["Flexiones", "Sentadillas", "Abdominales"]
#utilizamos while true para mantener el ciclo abierto
while True:
    #utilizamos input para pedir al usuario que ejercicio hizo
    print ("Que ejercicio hiciste hoy?")
    #usamos for para recorrer la lista de ejercicios
    for ejercicio in ejercicios:
        print(f"Buen trabajo, ejercicio registrado: {ejercicio}")
    if input("¿Quieres salir? (s/n): ") != "n":
        break
    else:
        print("Ese ejercicio no está en la lista, intenta de nuevo.")

    #correccion del ejercicio
    # 1. Definimos la lista
ejercicios = ["Flexiones", "Sentadillas", "Abdominales"]

while True:
    # 2. Capturamos la respuesta en una variable (el input fuera del for)
    print("\n--- Menú de Entrenamiento ---")
    usuario_hizo = input("¿Qué ejercicio hiciste hoy? ")

    # 3. Verificamos si quiere salir primero
    if usuario_hizo.lower() == "salir":
        print("¡Saliendo! Buen entrenamiento, Alexis.")
        break

    # 4. Buscamos si lo que escribió está en la lista
    if usuario_hizo in ejercicios:
        print(f"¡Buen trabajo! {usuario_hizo} registrado con éxito.")
    else:
        print(f"Ese ejercicio '{usuario_hizo}' no está en el plan de hoy.")