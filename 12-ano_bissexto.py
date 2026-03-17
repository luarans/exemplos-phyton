import os
os.system("cls")

#1-Entrada
ano = int(input("Digite o ano desejado: "))

#2-Processamento
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")

else:
    print("O ano não é bissexto.")

input("Pressione a tecla <enter> para encerrar.")