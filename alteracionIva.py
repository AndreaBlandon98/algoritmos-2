iva = float(input("ingrese el IVA"))
precio_sin_iva = 0
precio_con_iva = 0

for i in range(1,11):
    precio = float(input(f"ingrese el precio del producto {i}: "))
    precio_sin_iva += precio
    precio_con_iva += precio * (1 + iva)

print(f"el precio total antes de aplicar el IVA es: ${precio_sin_iva}")
print(f"el precio total despues de aplicar el IVA es: ${precio_con_iva}")