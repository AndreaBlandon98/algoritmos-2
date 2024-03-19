n = int(input("ingresa un numero entero: "))
factorial = 1
for i in range (1, n + 1):
    factorial *= i
print(f"el factorial de {n} es: {factorial}")
