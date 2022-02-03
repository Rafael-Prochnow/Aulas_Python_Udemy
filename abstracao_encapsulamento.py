"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes

Encapsular -> cápsula

        classe
|-----------------------------|
|     atributos e métodos     |
|_____________________________|

# Relembrando Atributos/Métodos privados em Python
Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe,
mas python não bloqueia este acesso fora da classe. Com Python aconcete um fenômeno chaamdo Name Mangling,
que faz uma alteração na forma de se acesssar os alements privados, corforme:

_Classe__elemento

Abistração, em POO, é o ato de expor apenas dados relevantes de um classe, escondendo atributos
e métodos privados de usuário
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência de quem realiza
        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Testando
conta1 = Conta('Geek', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Rafael', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)
conta2.extrato()
conta1.extrato()

