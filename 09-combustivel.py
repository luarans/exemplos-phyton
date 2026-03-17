import os
os.system("cls")

#1-Entrada
q_km = float(input("Digite a quantidade de km percorridos: "))
litros = float(input("Digite a quantidade de litros consumidos: "))

#2-Processamento
consumo = q_km / litros
print("O consumo médio do veículo é: ", consumo,"km/l.")

#3-Saida
input("Pressione a tecla <enter> para encerrar.")