menu = """

Bem-vindo ao DioBank, por favor selecione uma das operações abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Operação não realizada! O valor do depósito é inválido.")

    elif opcao == "2":
        saque = float(input("Informe o valor a ser sacado: "))

        if saldo == 0 or saque > saldo:
            print("Operação não realizada! Saldo em conta insuficiente.")

        elif saque > limite:
            print("Operação não realizada! O valor do saque excede o limite permitido.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação não realizada! Limite de saques diários excedido.")
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "3":
        print("\n====== Dio Bank - Extrato ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n================================")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema.")
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")