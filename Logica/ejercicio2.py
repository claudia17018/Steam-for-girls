""" Pedir al usuario que introduzca un número y mostrar su tabla de multiplicar del 1 al 10. """

numero = int(input("Introduce un número: "))

for i in range(1,11):
    print(numero * i)