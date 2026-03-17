import os
os.system("cls")

#1-Entrada
q_produtos = int(input("Digite a quantidade de produtos em estoque: "))

#2-Processamento
if q_produtos <= 5:
    print("O estoque está baixo.")

elif q_produtos > 5:
    print("O estoque está bom.")

#3-Saida
input("Pressione a tecla <enter> para encerrar.")