import os
os.system("cls")

#1-Entrada
veiculo = input("Digite o tipo do veículo: ")
#2-Processamento
if veiculo == "carro":
    valor = 10
    print("O valor do pedágio para o veículo é: ", valor,"R$.")

elif veiculo == "moto":
    valor = 5
    print("O valor do pedágio para o veículo é: ", valor,"R$.")

elif veiculo == "caminhão":
    valor = 20
    print("O valor do pedágio para o veículo é: ", valor,"R$.")

else:
    print("Tipo de veículo inválido.")

#3-Saida
input("Pressione a tecla <enter> para encerrar.")