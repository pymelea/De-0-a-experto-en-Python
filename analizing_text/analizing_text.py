# Analizador de texto

text = input("Ingrese un texto que desee analizar: ")
letras = []

text = text.lower()

letras.append(input("Ingresa la primera letra del texto: "))
letras.append(input("Ingresa la segunda letra del texto: "))
letras.append(input("Ingresa la tercera letra del texto: "))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = text.count(letras[0])
cantidad_letras2 = text.count(letras[1])
cantidad_letras3 = text.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = text.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = text[0]
letra_final = text[-1]

print(f"La letra iniciales '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
text_invertido = ' '.join(palabras)

print(f"El texto invertido es: '{text_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")

buscar_python = 'python' in text
dic = {True: 'SI', False: 'NO'}
print(f"La palabra 'Python': {dic[buscar_python]} se encuentra en el texto")
