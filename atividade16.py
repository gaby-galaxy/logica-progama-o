positivos = 0
for a in range(10):
    numero = int(input(f"Digite o {a+1}º número"))
    if numero > 0:
        positivos += 1
print("Quantidade de números positivos", positivos)