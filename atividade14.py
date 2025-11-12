import random
secreto = random.randint(1, 20)
tentativa = 0
acertou = False
while not acertou:
    tentativa = int(input("Adivinhe o número (entre 1 e 20)"))
    if tentativa == secreto:
        print("Parabéns! Você acertou!")
        acertou = True
    else:
        print("Errado! Tente novamente.")