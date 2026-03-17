import os
import random
os.system("cls")

#1-Entrada
numero = float(input("Digite seu palpite: "))

#2-Processamento
numero_secreto = random.randint(1, 100)
if numero == numero_secreto:
    print("Parabéns! Você acertou o número secreto!")

else:
    print("Que pena! Você errou. O número secreto era: ", numero_secreto)

#3-Saida
input("Pressione a tecla <enter> para encerrar.")
