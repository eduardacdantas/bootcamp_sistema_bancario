from funcoes import depositar, sacar, cadastrar_novo_usuario, criar_usuario, criar_conta


menu = """
[a] Adicionar novo cliente
[c] Criar conta corrente
[l] listar contas
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

usuarios = []
contas = []




while True:
    opcao = input(menu)
    if opcao == "d":
        saldo, extrato = depositar(saldo_inicial=saldo, extrato=extrato)
    
    elif opcao == "s":
        print("Saque")
        print(f"Você já realizou {numero_saque}")
        saldo, numero_saque, extrato = sacar(numero_saque=numero_saque, saldo=saldo, limite_saque=LIMITE_SAQUES, limite=limite, extrato=extrato)

    elif opcao == "e":
        print(extrato)
    
    elif opcao == "a":
        novo_usuario = criar_usuario()
        cadastrar_novo_usuario(lista_de_usuarios=usuarios, novo_usuario=novo_usuario)
        print(usuarios)
    
    elif opcao == "c":
        criar_conta(lista_de_contas=contas, lista_de_usuarios=usuarios)

    elif opcao == "l":
        print(contas)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecionar novamente a operação desejada.")

