import os
os.system("cls")

# 1 Etapa - Entrada
numero01 = float(input("Digite um número: "))
numero02 = float(input("Digite o segundo número: "))

operacao = input("EScolha a operação: ")

# 2 Etapa - Processamento
#SE
if(operacao == "+"):
    resultado = numero01 + numero02

#SENAO SE

elif(operacao == "-"):
    resultado = numero01 - numero02

elif(operacao == "*"):
    resultado = numero01 * numero02

elif(operacao == "/"):
    resultado = numero01 / numero02

else:
    print("Operação inválida.")

# 3 Etapa - Saida

print("O resultado é: ", resultado)

input("Pressione a tecla <enter> para encerrar.")