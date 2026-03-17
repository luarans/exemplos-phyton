import os
os.system("cls")

#1-Entrada
usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")               

#2-Processamento
if usuario == "admin" and senha == "123":
    print("O seu login foi realizado com sucesso!")

else:
    print("Usuário ou senha incorretos. Tente novamente.")
