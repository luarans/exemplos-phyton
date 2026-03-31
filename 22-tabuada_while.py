import os
os.system("cls")

numero = int(input("Digite um número para a tabuada: "))
limite_tabuada = int(input("Digite o limite da tabuada: "))

contador = 0
while(contador <= 10):
    print(f"Contador:{contador} x {numero} = {contador * numero}")
    contador+=1   
