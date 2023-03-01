""" Pedir al usuario que introduzca una lista de palabras y
 contar cuántas palabras tienen una longitud mayor a 5 caracteres."""

words = input("Ingrese una lista de palabras separadas por comas: ")

word_list =  words.split(",")

list = []

for word in word_list:
    if len(word) > 5:
        list.append(word)

print("Las palabras que tienen una longitud mayor a 5 caracteres son: ", len(list))
print("Las palabras son", list)