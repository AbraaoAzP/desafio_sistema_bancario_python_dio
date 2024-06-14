menu = """

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

        else:
            print("Operação não realizada! O valor do depósito é inválido.") 

    elif opcao == "2":
        saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Saldo em conta insuficiente!")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saque excede o limite permitido.")

        elif excedeu_saques:
            print("Operação não realizada! Limite de saques diários excedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido.")


    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n=============================")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema.")
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")