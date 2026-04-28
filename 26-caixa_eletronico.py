import os
os.system("cls")

# 1 Etapa - Entrada
saldo = 1000
rodando = True
while rodando:
    print("Bem-vindo ao caixa eletrônico!")
    print("1 - Consultar saldo")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    # 2 Etapa - Processamento
    if escolha == "1":
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif escolha == "2":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo = :.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    elif escolha == "3":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo += valor_deposito
        print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")

    elif escolha == "4":
        rodando = False
        print("Obrigado por usar o caixa eletrônico. Até logo!")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")