n = int(input("Digite um número"))

a = 1
soma = 0

while a <= n:
    soma += a
    a += 1

print("A soma dos números de 1 até", n, "é", soma)