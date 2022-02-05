"""
POO - Herança (Inheritance)

A ideia de Herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe que passa
a herdar atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionário
    - nome
    - sobrenome
    - cpf
    - matrícula

Perguntar: Existe alguma entidade genérica o suficiente para enxapsular os atributos
e métodos comuns a outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Rafael', 'Andreolli', '469.989.068-70', 12345)
funcionario1 = Funcionario('Rogerio', 'Correia', '309.989.068-70', 1123)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# OBS: Quando uma classe herda uma classem, ela herda todos os atributos e métodos de classe herdados

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super CLasse;
    - Classe Mãe
    - Classe Pai;
    - CLasse Base;
    - Classe Genérica

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente/Funcionário]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;



class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Rafael', 'Andreolli', '469.989.068-70', 12345)
funcionario1 = Funcionario('Rogerio', 'Correia', '309.989.068-70', 1123)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


# Sobrescrita de Métodos (Overriding)
Sobrescrita de Métodos, ocorre quando reescrevemos/reiplementamos um método presente na super classe em
classes filhas
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Rafael', 'Andreolli', '469.989.068-70', 12345)
funcionario1 = Funcionario('Rogerio', 'Correia', '309.989.068-70', 1123)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
