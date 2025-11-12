a = int(input("Digite o valor de a"))
b = int(input("Digite o valor de b"))
print(f"Números ímpares entre {a} e {b}:")
for numero in range(a + 1, b):
    if numero % 2 != 0:
        print(numero)