def deposit(balance, value, statement):
    if value > 0:
        balance += value
        statement += f'Depósito: $ {value}\n'
    else:
        print('O valor informado é inválido!')
    return balance, statement

def withdraw(*, balance, value, statement, limit, num_withdrawals, withdrawal_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = num_withdrawals >= withdrawal_limit

    if exceeded_balance:
        print('Você não tem saldo suficiente!')
    elif exceeded_limit:
        print('O valor do saque excede o limite!')
    elif exceeded_withdrawals:
        print('Número máximo de saques excedido!')
    elif value > 0:
        balance -= value
        statement += f'Saque: $ {value}\n'
        num_withdrawals += 1
    else:
        print('O valor informado é inválido!')

    return balance, statement


def print_statement(balance, *, statement):
    print('Não foram realizadas movimentações.' if not statement else statement)
    print(f'Saldo: $ {balance}')

def filter_user(cpf, users):
    filtered_users = [user for user in users if user['CPF'] == cpf]
    return filtered_users[0] if filtered_users else None

def create_user(users):
    cpf = input('Informe o CPF: ')
    user = filter_user(cpf, users)
    if user:
        print('Já existe um usuário com este CPF!')
        return
    name = input('Informe o nome completo: ')
    birth_date = input('Informe a data de nascimento: ')
    address = input('Informe o endereço: (Avenida, Rua - Número - Bairro - Cidade/UF): ')
    users.append({'Nome': name, 'Data de Nascimento': birth_date, 'Endereço': address, 'CPF': cpf}) 
    print('Criado com sucesso!')

def create_account(branch, account_number, users):
    cpf = input('Informe o CPF: ')
    user = filter_user(cpf, users)
    if user:
        print('Criado com sucesso!')
        return {'Agência': branch, 'Número da Conta': account_number, 'Usuário': user}
    else:
        print('Usuário não encontrado, cadastre-o!')

def list_accounts(accounts):
    for account in accounts:
        desc = f'''
            Agência: {account['Agência']}
            Conta: {account['Número da Conta']}
            Titular: {account['Usuário']['Nome']}
            '''
        print(desc)