soma = 0
for a in range(5):
    nota = float(input(f"Digite a {a+1}ª nota"))
    soma += nota
media = soma / 5
print("Média final:", media)