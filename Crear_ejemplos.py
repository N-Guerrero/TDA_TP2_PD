import random

# Leer el diccionario
with open("Ejemplos\gigante.txt", "r") as file:
    palabras = [line.strip() for line in file]

# Generar mensajes aleatorios
num_mensajes = 2000  # Cantidad de mensajes a generar
longitud_min = 10    # Mínimo de palabras por mensaje
longitud_max = 11   # Máximo de palabras por mensaje

mensajes = []
for _ in range(num_mensajes):
    num_palabras = random.randint(longitud_min, longitud_max)
    mensaje = "".join(random.choices(palabras, k=num_palabras))
    mensajes.append(mensaje)

# Guardar los mensajes en un archivo
with open("Ejemplos_random\mensajes_2000_gigante_largo.txt", "w") as file:
    for mensaje in mensajes:
        file.write(mensaje + "\n")

print("Mensajes generados en 'mensajes.txt'")