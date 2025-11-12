produto = 1
for a in range(10):
    numero = int(input(f"Digite o {a+1}º número"))
    produto *= numero
print("Produto dos números:", produto)