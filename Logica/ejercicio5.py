""" Pedir al usuario que introduzca una lista 
de números y encontrar el número más grande en la lista."""
aux = 0
numbers = input("Introduce una lista de numeros separados por coma ")
number_list = numbers.split(",")
num_integer = [int(n) for n in number_list]

for i in num_integer:
    if i > aux:
        aux = i

print("El numero mayor de la lista es:", i)
