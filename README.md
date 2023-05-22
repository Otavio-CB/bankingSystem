# Sistema Bancário Simples em Python

Este projeto é um sistema bancário simples desenvolvido em Python, como proposto pela plataforma DIO (Digital Innovation One). O objetivo do projeto é criar um programa que simule as operações básicas de um sistema bancário, como fazer depósitos, saques, consulta de extrato e saldo.

## Funcionalidades

- Depósito em conta
- Saque de conta
- Consulta de extrato
- Criar Usuário
- Criar Conta
- Lista de Contas

## Como utilizar o programa

Ao iniciar o programa, você terá as seguintes opções:

- [1] Depositar
- [2] Sacar
- [3] Extrato
- [4] Criar Usuário
- [5] Criar Conta
- [6] Lista de Contas
- [7] Sair

### Depositar

Ao selecionar a opção `[1] Depositar`, você deverá informar o valor que deseja depositar. O programa irá verificar se o valor é válido e, se sim, será adicionado ao saldo da conta. Caso contrário, será exibida uma mensagem informando que o valor é inválido.

### Sacar

Ao selecionar a opção `[2] Sacar`, você deverá informar o valor que deseja sacar. O programa irá verificar se o valor é válido e se existem fundos suficientes na conta para realizar o saque. Além disso, também serão verificados o limite de saques e o limite de saldo. Se todas as condições forem atendidas, o valor será subtraído do saldo da conta e o número de saques será atualizado. Caso contrário, serão exibidas mensagens de erro informando o motivo.

### Extrato

Ao selecionar a opção `[3] Extrato`, o programa irá exibir o extrato das movimentações realizadas, incluindo depósitos e saques, assim como o saldo atual da conta.

### Criar Usuário

Ao selecionar a opção `[4] Criar Usuário`, você deverá informar as informações necessárias para que seja possível criar o seu usuário, possibilitando a criação da sua conta.

### Criar Conta

Ao selecionar a opção `[5] Criar Conta`, você deverá fornecer seu CPF cadastrado na `[4] Criar Usuário`, e o programa irá criar sua conta.

### Lista de Contas

Ao selecionar a opção `[6] Lista de Contas`, o programa irá exibir todas as contas criadas.

### Sair

Ao selecionar a opção `[7] Sair`, o programa será encerrado.


### Pré-requisitos

- Requer o Python 3.7 ou superior.
