"""Crear un juego en el que el programa elige un número aleatorio entre 1 y 100, y 
el usuario tiene que adivinar ese número en un número limitado de intentos. 
El programa debe proporcionar pistas (por ejemplo, 
"El número es más grande que 50") para ayudar al usuario a adivinar el número."""

import random

number = random.randint(1,100)

number_of_attemps = int(input("Ingresa el numero de intentos que quiere tener para adivinar"))

counter = 1
print(number)

while counter <= number_of_attemps:
    user_number = int(input("Ingrese un numero"))

    if user_number == number:
        print("Perfect lo has adivinado el numero es: ", number )
        break
    elif user_number < number:
        print("El número es más grande que ", user_number)
    else:
        print("El número es más pequeño que ", user_number)
    counter += 1 