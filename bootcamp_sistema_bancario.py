menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
mensagem_extrato = "Foi realizada uma operação de {operacao} no valor de R$ {valor} :) \n"

while True:
    opcao = input(menu)

    if opcao == "d":
        print("deposito")
        valor = int(input("Qual valor você gostaria de depositar? "))
        if valor < 0:
            print("Insira um depósito positivo, por favor, não aceitamos depositos negativos.")
        else:
            saldo += valor
            extrato += mensagem_extrato.format(operacao="deposito", valor=valor)
            print(f"O seu saldo é: {saldo}")
        
        
    
    elif opcao == "s":
        print("Saque")
        if numero_saque == LIMITE_SAQUES:
            print("Você atingiu o limite máximo de saque diário")
            continue
        saque = int(input("Você só tem permissão de sacar 500 reais 3 vezes, quanto você gostaria de sacar?:"))
        if saque > limite:
            print("Limite máximo 500 reais por saque")
        
        elif saque > saldo:
            print(f"Seu saldo é insuficiente para essa operação, você só tem {saldo} na sua continha")
        else:
            saldo = saldo - saque
            numero_saque +=1
            extrato += mensagem_extrato.format(operacao="saque", valor=saque)
            print(f"Só te resta R$ {saldo}, amigo. Boa sorte!")

    
    elif opcao == "e":
        print(extrato)

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecionar novamente a operação desejada.")
