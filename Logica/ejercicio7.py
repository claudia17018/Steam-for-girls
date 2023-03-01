"""Generar una lista de 100 números aleatorios y ordenarlos 
de menor a mayor utilizando el algoritmo de burbuja."""

import random

numbers = []
aux = 0

for i in range(10):
    number = random.randint(1, 100)
    numbers.append(number)

print(numbers)
total_items = len(numbers)

for i in range(total_items):
    for j in range(0, total_items-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Lista de números aleatorios ordenados de menor a mayor: ",numbers)

