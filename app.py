#Variaveis

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0

menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

while True:

    opcao = int(input(menu))
    print()

    if opcao == 1:
        
        print('######################### Deposito ##########################')
        print()
        deposito = float(input('Informe o valor que deseja depositar: R$ '))
        print()
        print('##############################################################')
        print()

        if deposito <= 0:

            print('Não é possivel depositar saldos negativo')
            print('Por gentileza, tente realizar a operação novamente')

        else:
            # Regitra operação no extrato
            saldo += deposito
            extrato += f'Deposito R$ {deposito:.2f}\n'

            print(f'Valor depositado com sucesso R$ {deposito:.2f}')
            print()
            print('##############################################################')

    elif opcao == 2:

        print('######################### Saque ##########################')
        print()
        saque = float(input('Informe o valor que deseja sacar: R$ '))
        print()

        if numero_saques >= LIMITE_SAQUES:

            print('Limites de saques diarios excedidos')
            print()
            print('##############################################################')            

        elif saque > limite:
            print('Saque fora do limite autorizado')
            print()
            print('##############################################################')
            
        elif saque > saldo:
            print('Valor indisponível para saque')
            print()
            print('##############################################################')
            
        else:
            numero_saques += 1
            #print(numero_saques) #teste
            saldo -= saque
            extrato += f'Saque: R$ -{saque:.2f}\n'
            print(f'Saque realizado com sucesso R$ -{saque:.2f}')
            print()
            print('##############################################################')

    elif opcao == 3:

        print('######################### Extrato ##########################')
        print()

        if extrato == '':
            print(f'Saldo atual: R$ {saldo:.2f}')
            print()
            print('Extrato atual')
            print('Não foram realizadas movimentações')
            print()
            print('##############################################################')
        else:
            print(f'Operações realizadas:\nR$ {extrato}')
            print()
            print(f'Saldo em conta: R$ {saldo:.2f}')
            print('##############################################################')

    elif opcao == 0:
        print('Sair')
        break
    else:
        print('Opção inválida, por favor selecione a operação desejada.')
