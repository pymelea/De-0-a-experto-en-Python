from random import shuffle

# Lista Inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitos
shuffle(palitos)
def mezclar(lista):
    shuffle(lista)
    return lista

print(mezclar(palitos))


# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

intento1 = probar_suerte()
print(intento1)

# Comprobar Intento
def chequear_intento(lista, intento):
    if lista[intento - 1 ] == '-':
        print("Pinguinos")
    # elif lista[intento - 1 ] == '--':
    #     print("Perritos")
    # elif lista[intento - 1 ] == '---':
    #     print("Pericos")
    else:
        print("Te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)