contador = 0

for numero in range(1, 101):
    if numero % 3 == 0:
        contador += 1

print("Quantidade de múltiplos de 3 entre 1 e 100", contador)