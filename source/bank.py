import utils.transactions as util
def main():
    WITHDRAWAL_LIMIT = 3
    BRANCH = '0001'
    balance = 0
    limit = 500
    statement = ''
    num_withdrawals = 0
    users = []
    accounts = []

    while True:
        menu = f'''
[1] Deposito
[2] Saque
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Lista de Contas
[7] Sair '''
        print(menu)
        option = input('Selecione uma opção: ')

        if option == '1':
            value = float(input('Digite o valor do depósito: '))
            balance, statement = util.deposit(balance, value, statement)
        elif option == '2':
            value = float(input('Digite o valor do saque: '))
            balance, statement = util.withdraw(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                num_withdrawals=num_withdrawals,
                withdrawal_limit=WITHDRAWAL_LIMIT
            )
        elif option == '3':
            util.print_statement(balance, statement=statement)
        elif option == '4':
            util.create_user(users)
        elif option == '5':
            number_account = len(accounts) + 1
            account = util.create_account(BRANCH, number_account, users)
            if account:
                accounts.append(account)
        elif option == '6':
            util.list_accounts(accounts)
        elif option == '7':
            break
        else:
            print('Operação Inválida')
main()