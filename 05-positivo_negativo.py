import os
os.system("cls")

#1 Etapa - Entrada
numero01 = float(input("Digite um número: "))

#2 Etapa - Processamento

if numero01 > 0:
    print("O número é positivo.")

elif numero01 < 0:
    print("O número é negativo.")

else:
    print("O número é zero.")
    print("O programa está finalizado.")

