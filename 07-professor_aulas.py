import os
os.system("cls")

#1-Entrada
professor = input("Digite o nível do professor: ")
q_aulas = float(input("Digite a quantidade de aulas por semana: "))

#2-Processamento
if professor == "1":
    salario = q_aulas * 12
    print("O salário do professor será: ", salario,"R$.")

elif professor == "2":
    salario = q_aulas * 17
    print("O salário do professor será: ", salario,"R$.")

elif professor == "3":
    salario = q_aulas * 25
    print("O salário do professor será: ", salario,"R$.")

#3-Saida
input("Pressione a tecla <enter> para encerrar.")