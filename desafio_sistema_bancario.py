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
        
        print("Informe o valor a ser depositado: ")

        deposito = int(input())
        saldo += deposito
        extrato = deposito

        print("Depósito realizado com sucesso!")

    elif opcao == "2":

        print("Informe o valor a ser sacado: ")
        saque = int(input())

        if saldo == 0 or saque > saldo:
            print("Não é possível realizar o saque! Saldo insuficiente.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Não é possível realizar o saque! O limite diário permitido foi atingido!")
        
        elif saque <= limite:
            saldo -= saque
            extrato = saque
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Não é possível realizar o saque! O valor excede o limite permitido!")

    elif opcao == "3":
        print("Extrato")
        print(f"R${extrato:.2f}")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema.")
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")