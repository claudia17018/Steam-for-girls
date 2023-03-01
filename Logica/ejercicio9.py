"""Pedir al usuario que introduzca una lista de palabras y ordenarlas alfabéticamente."""

list_words = input("Ingresa una lista de palabras separadas por comas ").split(",")

list_sort = list_words.sort()

print(list_sort)

print("Las palabras ordenadas alfabéticamente son:")
for word in list_words:
    print(word)
