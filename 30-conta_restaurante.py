import os
os.system("cls")

print("Bem-vindo ao App Minha Conta!")
valor_conta = float(input("Digite o valor da conta: "))
quantidade = int(input("Informe a quantidade de pessoas: "))

valor_por_pessoa = valor_conta / quantidade

print("O valor a ser pago por cada pessoa é: ", valor_por_pessoa, "R$.")
input("Pressione a tecla <enter> para encerrar.")