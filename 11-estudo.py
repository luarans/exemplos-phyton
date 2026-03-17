import os
os.system("cls")

#1-Entrada
horas = float(input("Digite por quantas horas você estudou: "))

#2-Processamento
if horas < 2:
    print("Você estudou pouco, estude mais!")

elif horas >= 2 and horas <= 5:
    print("Você estudou o suficiente, continue assim!")

elif horas > 5:
    print("Você estudou muito, cuidado para não se cansar!")

#3-Saida
input("Pressione a tecla <enter> para encerrar.")