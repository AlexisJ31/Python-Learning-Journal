# Crea un archivo llamado for_practice.py en VS Code
# un bucle for que reccore una lista de jugadores de fútbol del FC Barcelona
crack_players = ["Messi", "Lamine Yamal", "Pedri"]

for player in crack_players:
    print(f"{player} es un crack del Barça")

#ejemplo 2
# Esto imprimirá del 0 al 4 (el 5 no se incluye)
for i in range(5):
    print(f"Vuelta número: {i}")

#Ejemplo 3
#utilizare el ciclo for y el if para este ejercicio
#definimos la lista
marcas = ["Smansung", "Nokia", "Sony", "Apple", "Huawei"]
#recorremos la lista con un for
for marca in marcas:
    #usamos un if para verificar si la marca es Apple
    if marca == "Apple":
        print(f"{marca} es la mejor marca de teléfonos")
    else:
        print(f"{marca} es una buena marca, pero no como Apple")

#alternativa para retroceder en el for
for marca in reversed(marcas):
    print(f"Marca desde el final: {marca}")
