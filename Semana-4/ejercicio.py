import calculadora

try:
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    resultado = calculadora.division(a, b)
    
except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

except Exception as e:
    print(f"Ocurrió un error: {e}")

else:
    print(f"El resultado de la división es {resultado}")
finally:
    print("El programa ha terminado.")