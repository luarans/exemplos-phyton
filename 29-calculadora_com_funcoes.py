import os
os.system("cls")
print("Seja bem vindo a super calculadora 2.0 pro max!")

def somar(numero01, numero02):
    resultado = numero01 + numero02
    return resultado

def subtrair(numero01, numero02):
    resultado = numero01 - numero02
    return resultado

def multiplicar(numero01, numero02):
    resultado = numero01 * numero02
    return resultado

def dividir(numero01, numero02):
    resultado = numero01 / numero02
    return resultado

numero01 = int(input("Informe o primeiro número: "))
numero02 = int(input("Informe o segundo número: "))

print("Escolha uma das opções abaixo: ")
print("[1] - Somar")
print("[2] - Subtrair")
print("[3] - Multiplicar")
print("[4] - Dividir")
opcao = int(input("Escolha uma opção: "))

if(opcao == 1):
    # Chamar a função de soma
    print(f"A soma é: {somar(numero01, numero02)}")
elif(opcao == 2):
    # Chamar a função de subtração
    print(f"A subtração é: {subtrair(numero01, numero02)}")
elif(opcao == 3):
    # Chamar a função de multiplicação
    print(f"A multiplicação é: {multiplicar(numero01, numero02)}")
elif(opcao == 4):
    # Chamar a função de divisão
    print(f"A divisão é: {dividir(numero01, numero02)}")
  
else:
    print("Opção inválida.")

input("Pressione a tecla <enter> para encerrar.")