# Sistema Bancário Simples em Python

Este projeto é um sistema bancário simples desenvolvido em Python, como proposto pela plataforma DIO (Digital Innovation One). O objetivo do projeto é criar um programa que simule as operações básicas de um sistema bancário, como fazer depósitos, saques e transferências entre contas.

## Funcionalidades

- Depósito em conta
- Saque de conta
- Transferência entre contas
- Consulta de saldo
- Consulta de extrato

## Como utilizar o programa

Ao iniciar o programa, você terá as seguintes opções:

- [1] Depositar
- [2] Sacar
- [3] Extrato
- [4] Sair

### Depositar

Ao selecionar a opção `[1] Depositar`, você deverá informar o valor que deseja depositar. O programa irá verificar se o valor é válido e, se sim, será adicionado ao saldo da conta. Caso contrário, será exibida uma mensagem informando que o valor é inválido.

### Sacar

Ao selecionar a opção `[2] Sacar`, você deverá informar o valor que deseja sacar. O programa irá verificar se o valor é válido e se existem fundos suficientes na conta para realizar o saque. Além disso, também serão verificados o limite de saques e o limite de saldo. Se todas as condições forem atendidas, o valor será subtraído do saldo da conta e o número de saques será atualizado. Caso contrário, serão exibidas mensagens de erro informando o motivo.

### Extrato

Ao selecionar a opção `[3] Extrato`, o programa irá exibir o extrato das movimentações realizadas, incluindo depósitos e saques, assim como o saldo atual da conta.

### Sair

Ao selecionar a opção `[4] Sair`, o programa será encerrado.


### Pré-requisitos

- Requer o Python 3.7 ou superior.
