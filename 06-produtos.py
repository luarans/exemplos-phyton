import os
os.system("cls")
#1-Entrada
produto = input("Digite o produto: ")
quantidade = float(input("Digite a quantidade: "))
preco = float(input("Digite o preço unitário do produto: "))

#2-Processamento
resultado = quantidade * preco
print("O total da compra será: ", resultado,"R$.")

#3-Saida
if quantidade <= 5:
    desconto = 2
    total = resultado - desconto
    print("O total da compra com desconto será: ", total)

elif quantidade >5 and quantidade <= 10:
    desconto = 3
    total = resultado - desconto
    print("O total da compra com desconto será: ", total)

elif quantidade > 10:
    desconto = 5
    total = resultado - desconto
    print("O total da compra com desconto será: ", total,"R$")

input("Pressione a tecla <enter> para encerrar.")





