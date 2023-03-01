tabla_inicio = int(input("Ingrese el número de la tabla de inicio: "))
tabla_final = int(input("Ingrese el número de la tabla final: "))

for i in range(tabla_inicio, tabla_final + 1):
    print("Tabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("")
