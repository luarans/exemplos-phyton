import os
import random
os.system("cls")

#Passo 1 - Entrada
pokemon = input("Digite o nome do seu pokemon: ")
pokemon_2 = input("Digite o nome do pokemon adversário: ")

vida_pokemon = 100
vida_pokemon_2 = 100
ataque_pokemon = -10
ataque_pokemon_2 = -10
curar_pokemon = 5
fugir_pokemon = 0

#Passo 2 - Processamento
while(vida_pokemon > 0 and vida_pokemon_2 > 0):
    print(f"Vida do {pokemon}: {vida_pokemon}")
    print(f"Vida do {pokemon_2}: {vida_pokemon_2}")
    acao = input("Digite a ação desejada (atacar, curar ou fugir): ")

    if(acao == "atacar"):
        vida_pokemon_2 += ataque_pokemon
        print(f"{pokemon} atacou {pokemon_2} e causou 10 de dano!")

    elif(acao == "curar"):
        vida_pokemon += curar_pokemon
        print(f"{pokemon} se curou e recuperou 5 de vida!")

    elif(acao == "fugir"):
        print(f"{pokemon} fugiu da batalha!")
        break

    else:
        print("Ação inválida. Tente novamente.")

    if acao in ["atacar", "curar"] and vida_pokemon_2 > 0:
        acao_2 = input(f"Digite a ação do {pokemon_2} (atacar, curar ou fugir): ")
        
        if acao_2 == "atacar":
            vida_pokemon += ataque_pokemon_2
            print(f"{pokemon_2} atacou {pokemon} e causou 10 de dano!")
        
        elif acao_2 == "curar":
            vida_pokemon_2 += curar_pokemon
            print(f"{pokemon_2} se curou e recuperou 5 de vida!")
        
        elif acao_2 == "fugir":
            print(f"{pokemon_2} fugiu da batalha!")
            break
        
        else:
            print("Ação inválida para o adversário. Tente novamente.")

if(vida_pokemon <= 0):
    print(f"{pokemon} foi derrotado! {pokemon_2} venceu a batalha!")
elif(vida_pokemon_2 <= 0):
    print(f"{pokemon_2} foi derrotado! {pokemon} venceu a batalha!")
else:
    print("Batalha interrompida.")

input("Pressione a tecla <enter> para encerrar.")

