mensagem_extrato = "Foi realizada uma operação de {operacao} no valor de R$ {valor} :) \n"

def depositar(saldo_inicial, extrato):
    saldo_final = saldo_inicial
    extrato_final = extrato
    print("deposito")
    valor = int(input("Qual valor você gostaria de depositar? "))
    if valor < 0:
        print("Insira um depósito positivo, por favor, não aceitamos depositos negativos.")
    else:
        saldo_final += valor
        extrato_final += mensagem_extrato.format(operacao="deposito", valor=valor)
        print(f"O seu saldo é: {saldo_final}")

    return saldo_final, extrato_final

def sacar(numero_saque, saldo, limite_saque, limite, extrato):
    saldo_final = saldo
    numero_saque_final = numero_saque
    extrato_final = extrato
    if numero_saque == limite_saque:
        print("Você atingiu o limite máximo de saque diário")
    else:
        saque = int(input("Você só tem permissão de sacar 500 reais 3 vezes, quanto você gostaria de sacar?:"))
        if saque > limite:
            print("Limite máximo 500 reais por saque")
        
        elif saque > saldo:
            print(f"Seu saldo é insuficiente para essa operação, você só tem R$ {saldo} na sua continha")
        else:
            saldo_final -= saque
            numero_saque_final +=1
            extrato_final += mensagem_extrato.format(operacao="saque", valor=saque)
            print(f"Só te resta R$ {saldo_final}, amigo. Boa sorte!")
    return saldo_final, numero_saque_final, extrato_final

#USUÁRIO


def receber_endereco():
    logradouro = input("Qual seu logradouro? ")
    num_casa = input("Qual é o número da sua residência? ")
    bairro = input("Qual bairro você mora? ")
    cidade = input("Qual a cidade que você mora? ")
    sigla_estado = input("Digite o UF da sua região? ")
    endereco = (f"{logradouro}, {num_casa} - {bairro} - {cidade}/{sigla_estado}")
    return endereco

def receber_cpf():
    while True:
        cpf = input("Qual é o seu cpf? ")
        if cpf.isnumeric():
            return cpf
        else:
            print("Amigo, o seu cpf está inválido. Digite apenas números.")


def criar_usuario():
    nome = input("Qual é o seu nome? ")
    data_nascimento = input("Quando você nasceu? ")
    cpf = receber_cpf()
    endereco = receber_endereco()
    
    usuario = {
        "nome": nome, 
        "nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    }
    return usuario

def usuario_existe(cpf, lista_de_usuarios):
    for usuario in lista_de_usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False

def cadastrar_novo_usuario(novo_usuario: dict, lista_de_usuarios: list):
    if usuario_existe(cpf=novo_usuario["cpf"], lista_de_usuarios=lista_de_usuarios):
        print("Já existe um usuário com um mesmo cpf")
        return
       
    lista_de_usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")


#Criar uma conta

def criar_conta(lista_de_contas: list, lista_de_usuarios: list):
    cpf = receber_cpf()
    if usuario_existe(cpf=cpf, lista_de_usuarios=lista_de_usuarios):
        numero_da_conta = len(lista_de_contas) + 1
        nova_conta = {
            "numero_conta": numero_da_conta,
            "agencia": "0001",
            "cpf": cpf
        }
        lista_de_contas.append(nova_conta)
        print("Bem vindo (a) ao nosso mundo. Conta criada com sucesso!")
    else:
        print("Não existe usuário para o cpf informado, por favor cadastre-se no nosso sistema para criar a sua conta.")







