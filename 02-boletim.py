
import os

os.system("cls")

print("Seja Bem Vindo ao seu boletim!")

nota01 = float(input("Digite sua primeira nota: "))
nota02 = float(input("Digite sua segunda nota: "))
nota03 = float(input("Digite sua terceira nota: "))

media = (nota01 + nota02 + nota03) / 3

print("Sua média foi: ", media)

if(media>=7):
    print("Você foi aprovado!")

elif(media>=4 and media<=6):
    print("Você está de recuperação.")

else:
    print("Você foi reprovado.")