nombre = input("Por favor dime tu nombre ")
ventas = int(input("Cuantas ventas totales de mes has tenido "))

comision = round(ventas * 13 / 100)

print(f"Hola {nombre}, tus comisiones de este mes son de $ {comision}")
