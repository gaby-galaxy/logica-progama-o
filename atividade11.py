numero = int(input("Digite um número inteiro"))
fatorial = 1
for a in range(1, numero + 1):
    fatorial *= a
print(f"{numero}! = {fatorial}")