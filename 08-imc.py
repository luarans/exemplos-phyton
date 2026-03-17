import os
os.system("cls")

#1-Entrada
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

#2-Processamento
imc = peso / (altura * altura)
print("O IMC é: ", imc)

#3-Saida
if imc < 16.9:
    print("Você está muito abaixo do peso.")  

elif imc >= 17 and imc < 18.4:
    print("Você está abaixo do peso.")

elif imc >= 18.5 and imc < 25:
    print("Você está com peso normal.")

elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")

elif imc >= 30 and imc < 35:
    print("Você está com obesidade grau I.")

elif imc >= 35 and imc <= 40:
    print("Você está com obesidade grau II.")

elif imc > 40:
    print("Você está com obesidade grau III.")

input("Pressione a tecla <enter> para encerrar.")