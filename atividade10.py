maior = None
menor = None
for a in range(10):
    numero = int(input(f"Digite o {a+1}º número"))
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
print("Maior número:", maior)
print("Menor número:", menor)