import os


# Criando as funções
# Criando a função que exibe o menu
def exibir_menu():
    print("=== Conversão de Moedas ===")
    print("[1] - Converter DÓLAR => REAL")
    print("[2] - Converter REAL => DÓLAR")
    print("[3] - Sair")

# Criando a função para limpar tela
def limpar_tela():
    os.system("cls")

# Criando as funções de conversão
def converter_dolar_para_real(quantia_dolar, cotacao):
    total_reais = quantia_dolar * cotacao
    return total_reais

def converter_real_para_dolar(quantia_real, cotacao):
    total_dolares = quantia_real / cotacao
    return total_dolares

# Função sair
def sair():
    exit()


# Criando a função main - principal
def main():
    limpar_tela()
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        quantia_dolar = float(input("Digite a quantia em dólares: ").replace(",", "."))
        cotacao = float(input("Informe a cotação: ").replace(",", "."))
        resultado = converter_dolar_para_real(quantia_dolar, cotacao)
        print(f"O total da conversão é: R$ {resultado:.2f}")

    elif opcao == 2:
        quantia_reais = float(input("Digite a quantia em reais: ").replace(",", "."))
        cotacao = float(input("Informe a cotação: ").replace(",", "."))
        resultado = converter_real_para_dolar(quantia_reais, cotacao)
        print(f"O total da conversão é: $ {resultado:.2f}")

    elif opcao == 3:
        sair()
    else:
        print("Opção inválida.")

# Chamando função main
main()
   
