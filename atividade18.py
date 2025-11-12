while True:
    print("\nMENU")
    print("1 - Somar dois números")
    print("2 - Subtrair dois números")
    print("3 - Sair")
    opcao = input("Escolha uma opção")
    if opcao == "1":
        a = float(input("Digite o primeiro número"))
        b = float(input("Digite o segundo número"))
        print("Resultado da soma", a + b)
    elif opcao == "2":
        a = float(input("Digite o primeiro número"))
        b = float(input("Digite o segundo número"))
        print("Resultado da subtração", a - b)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida tente novamente.")