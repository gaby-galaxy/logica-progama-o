soma = 0
quantidade = 0
while True:
    idade = int(input("Digite a idade (0 para parar)"))
    if idade == 0:
        break
    soma += idade
    quantidade += 1
if quantidade > 0:
    media = soma / quantidade
    print("Média das idades", media)
else:
    print("Nenhuma idade foi digitada")