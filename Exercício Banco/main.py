def main():
    saldo = float(input("Digite o saldo da conta: "))
    quantidadeSaques = 0
    while True:
        print("""
        Aplicativo de Banco

        [D]epositar
        [S]aque
        [E]xtrato bancário
        """)
        opcaoDesejada = input("Digite a opção desejada: ")
        match opcaoDesejada:
            case 'D':
                quantiaDeposito = float(input("Digite a quantidade que deseja depositar: "))
                if quantiaDeposito > 0:
                    saldo += quantiaDeposito
                    print(f"Depósito realizado! O saldo atual é de {saldo}")
                else:
                    print("A quantia de depósito é inválida")
            case 'S':
                if quantidadeSaques >= 3:
                    print("Não é possível sacar mais dinheiro, pois o limite é de 3 saques por dia")
                else:
                    valorSaque = float(input("Digite a quantidade desejada para o saque: "))
                    if valorSaque > saldo:
                        print("O valor que deseja extrair é maior do que o próprio extrato. Tentativa inválida")
                    elif valorSaque > 500:
                        print("O limite de dinheiro que pode ser sacado, por vez,  é de até 500 reais")
                    else:
                        saldo -= valorSaque
                        print(f"Saque realizado! A quantia atual de dinheiro é R${saldo}")
                        quantidadeSaques += 1
            case 'E':
                print(saldo)
            case _:
                print("Não foi possível identificar a opção. Digite novamente.")

main()