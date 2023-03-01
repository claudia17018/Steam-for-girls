"""Pedir al usuario que introduzca una cadena de texto y contar cuántas 
veces aparece cada letra en la cadena."""

text = input("Ingresa una cadena")
dict = {}

for i in text:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)