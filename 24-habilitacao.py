import os
os.system("cls")

print("Exemplo Habilitação")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if(idade >= 18):
    habilitacao = input("Você possui habilitação? (S/N): ")
    if(habilitacao == "S" or habilitacao == "s"):
        print("Você está habilitado para dirigir.")
    else:
        print("Você não está habilitado para dirigir.")
else:
    print("Você é menor de idade.")

resposta = input("Deseja de executar novamente o programa? (S/N): ")
if(resposta == "S" or resposta == "s"):
    os.system("python 24-habilitacao.py")
else:
    print("Programa encerrado.")