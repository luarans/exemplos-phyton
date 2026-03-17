import os
os.system("cls")

#1-Entrada
semaforo = input("Digite a cor do semáforo: ")

#2-Processamento
if semaforo == "verde":
    print("Pode passar!")

elif semaforo == "amarelo":
    print("Atenção! O semáforo está amarelo.")

elif semaforo == "vermelho":
    print("Pare! O semáforo está vermelho.")

else:
    print("Cor do semáforo inválida. Por favor, digite verde, amarelo ou vermelho.")

#3-Saida
input("Pressione a tecla <enter> para encerrar.")