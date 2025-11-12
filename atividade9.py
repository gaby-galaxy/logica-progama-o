somapares = 0
somaimpares = 0
for a in range(10):
    numero = int(input(f"Digite o {a+1}º número"))
    if numero % 2 == 0:
        somapares += numero
    else:
        somaimpares += numero
print("Soma dos pares:", somapares)
print("Soma dos ímpares:", somaimpares)