contador_0_20 = 0
contador_20_30 = 0
contador_30_40 = 0
contador_40_60 = 0
contador_mayores_60 = 0

for _ in range (10):
    edad = int(input("ingrese su edad: "))
    if edad >= 0 and edad <= 20:
        contador_0_20 += 1
    elif edad > 20 and edad <= 30:
        contador_20_30 += 1
    elif edad > 30 and edad <= 40:
        contador_30_40 += 1
    elif edad > 40 and edad <= 60:
        contador_40_60 += 1
    else:
        contador_mayores_60 += 1

        print(f"Personas en el rango de 0-20 años: {contador_0_20}")
        print(f"Personas en el rango de 20-30 años: {contador_20_30}")
        print(f"Personas en el rango de 30-40 años: {contador_30_40}")
        print(f"Personas en el rango de 40-60 años: {contador_40_60}")
        print(f"Personas mayores de 60 años: {contador_mayores_60}")
