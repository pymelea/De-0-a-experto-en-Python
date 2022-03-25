# from random import randint, uniform, random, choice, shuffle
#
# aleatorio = randint(1, 50)
# print(aleatorio)
#
#
# lista = []
# palabra = 'Python'
#
# for letra in palabra:
#     lista.append(letra)
#
#
# print(lista)
#
# # Comprension de Listas
# otras = []
#
# lista = [letra for letra in palabra]
# print(lista)
# otras = [ff for ff in 'python']
# print(otras)
# lista = [n if n * 2 < 10 else 'no' for n in range(randint(1,50)) ]
#
# print(lista)
#
# pies = [ 10,20,30,40,50]
# metros = [ p * 3.281 for p in pies]
# print(metros)
#
# serie = "N-02"
# match serie:
#     case "N-01":
#         print("Samsung")
#     case "N-02":
#         print("Nokia")
#     case "N-03":
#         print("Motorola")
#     case _:
#         print("No existe ese producto")

# Programar un juego
# Adivina un numero
from random import randint

intentos = 0
numero_secreto = randint(1, 50)

nombre = input("Cuál es tu nombre:  ")
print(f"Bueno {nombre}, estoy pensando en un número del 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Intenta un número:  "))
    intentos += 1
    if estimado < numero_secreto:
        print("El número es mayor")
    elif estimado > numero_secreto:
        print("El número es bajo")
    else:
        print(f"Felicidades {nombre}, has dado en el clavo el número es:  {intentos} intentos")
        break

if estimado != numero_secreto:
        print(f"Lo siento {nombre} no has acertado el número era: {numero_secreto}")