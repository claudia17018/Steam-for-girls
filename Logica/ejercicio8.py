numeros = input("Introduce una lista de números separados por comas: ")
numeros = [int(numero) for numero in numeros.split(",")]

# Encontrar el número máximo
maximo = max(numeros)

# Eliminar el número máximo de la lista
numeros_sin_maximo = [numero for numero in numeros if numero != maximo]

# Encontrar el número máximo en la lista sin el número máximo original
if numeros_sin_maximo:
    segundo_maximo = max(numeros_sin_maximo)
    print("El segundo número más grande es:", segundo_maximo)
else:
    print("No se ha encontrado un segundo número más grande.")
