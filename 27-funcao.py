import os
os.system("cls")

# Criando a primeira funcao
def escreva ( ):
    print("Olá, Mundo!")

#Criando uma função com parametros
def exibir_dados(nome, idade, email):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")
    print("="*108)

# Criando uma função com retorno
def somar(n1, n2):
    resultado = n1 + n2
    return resultado


# Chamando a função escreva
escreva()

# Chamando a função exibir_dados
exibir_dados("Caio", 38, "caio@email.com")
exibir_dados("Rebecca", 16, "rebeccacurisousa@gmail.com")

#Chamando função retorno
total = somar(10, 20)
print(f"O total será: {somar(10, 20)}")
