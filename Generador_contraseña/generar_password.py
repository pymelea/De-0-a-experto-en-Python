# Generador de contraseñas

import random


letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '_', '=', '?', '¿', '¡', '.', ',', ':', ';', '<', '>', '{', '}', '[', ']', '(', ')']

# Preguntar por el numero de letras, números y simbolos que quieres tomar en la contraseña

# Generar una contraseña aleatoria mezclando letras, números y símbolos de forma aleatoria

print("Bienvenidos al generador de contraseñas")

numero_letras = int(input("¿Cuantas letras? : "))
numero_numeros =  int(input("¿Cuantas números? : "))
numero_simbolos =  int(input("¿Cuantas símbolos? : "))

lists = []

for letra in range(1, numero_letras + 1):
    valor = random.choice(letras)
    lists.append(valor)

for numero in range(1, numero_numeros + 1):
    valor = random.choice(numeros)
    lists.append(valor)


for simbolo in range(1, numero_simbolos + 1):
    valor = random.choice(simbolos)
    lists.append(valor)

print(lists)
random.shuffle(lists)
print(lists)


password_final = ""
for caracter in lists:
    password_final = password_final + caracter

print(password_final)

