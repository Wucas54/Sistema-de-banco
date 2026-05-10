def menu():
    print("\n=== Conta do Banco ===")
    print("1 - Depositar")
    print("2 - Levantar")
    print("3 - Ver saldo")
    print("4 - Sair")

def ler_menu():
    while True:
        escolha = input("Escolha uma opção: ")
        if escolha in ['1','2','3','4']:
            return escolha
        else:
            print("Operação inválida!")

def depositar(saldo):
    try:
        valor = float(input("Quanto queres depositar? "))
    except ValueError: 
        print("Tens de colocar números!")
        return saldo
    
    if valor < 0.01: 
        print("Valor inválido!")
        return saldo
    if valor == 0:
        print("Valor inválido!")
        return saldo
    
    saldo += valor
    print("Depósito feito com sucesso!")
    return saldo

def levantar(saldo):
    try:
        valor = float(input("Quanto queres levantar? "))
    except ValueError:
        print("Tens de colocar números!")
        return saldo
    
    if valor < 0.01: 
        print("Valor inválido!")
        return saldo
    if valor <= 0:
        print("Valor inválido!")
        return saldo

    elif valor > saldo:
        print("Saldo insuficiente!")
        return saldo

    saldo -= valor
    print("Levantamento feito com sucesso!")
    return saldo

def ver_saldo(saldo):
    print(f"Saldo atual: {saldo}€")

def main():
    saldo= 0.0
    while True:
        menu()
        opcao = ler_menu()

        if opcao == '1':
            saldo = depositar(saldo)
        elif opcao == '2':
            saldo = levantar(saldo)
        elif opcao == '3':
            ver_saldo(saldo)
        elif opcao == '4':
            print("A sair...")
            break

main()