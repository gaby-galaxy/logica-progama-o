quantidade = 0
soma = 0
pares = 0
maior = None
menor = None
while True:
    numero = int(input("Digite um numero (0 para parar)"))
    if numero == 0:
        break
    quantidade += 1
    soma += numero
    if numero % 2 == 0:
        pares += 1
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
if quantidade > 0:
    media = soma / quantidade
    print("\nRESULTADOS")
    print("Quantidade de numeros digitados", quantidade)
    print("Media dos numeros", media)
    print("Maior numero", maior)
    print("Menor numero", menor)
    print("Quantidade de numeros pares", pares)
else:
    print("Nenhum numero foi digitado")