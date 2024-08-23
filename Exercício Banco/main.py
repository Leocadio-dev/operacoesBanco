# Declaração de variáveis globais padrão
nomeCliente = "Carlos Eduardo"
extrato = 2000.00
quantidadeSaques = 0

def main():

    while True:
        print("""
        Aplicativo de Banco

        [D]epositar
        [S]aque
        [E]xtrato bancário
        """)
        opcaoDesejada = input("O que deseja fazer?")
        match opcaoDesejada:
            case 'D':
                deposito()
            case 'S':
                saque()
            case 'E':
                consultarExtrato()
            case _:
                print("Não foi possível identificar a opção. Digite novamente.")
                
def deposito():
    quantia = float(input("Digite a quantidade desejada para o depósito: "))
    if quantia > 0:
        extrato += quantia
    else:
        print("A quantia é inválida.")

def saque():
    if quantidadeSaques < 3:
        print("Não é possível sacar mais dinheiro, pois o limite é de 3 saques por dia")
    else:
        quantia = float(input("Digite a quantidade desejada para o saque: "))
        if quantia > extrato:
            print("O valor que deseja extrair é maior do que o próprio extrato. Tentativa inválida")
        elif quantia > 500:
            print("O limite de saques é de 3 vezes por dia, e o limite de dinheiro que pode ser sacado é de até 500 reais")


main()