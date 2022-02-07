"""
POO - Herança Múltipla

Heraça Múltipla é a possibilidade de uma classe herdar de
múltiplas classes, fazendo com que a classe filha herde todos os atributos e métodos de todas as classes
herdadas

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Múltiderivação Direta
    - Múltiderivação Indireta

# Exemplo 1 - Múltiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass

# OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará.
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        print(f'Eu sou {self.__nome}')

    @property
    def nome(self):
        return self.__nome


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self.nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self.nome} da Terra'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

rafa = Pinguim('Rafa')
print(rafa.andar())
print(rafa.nadar())
print(rafa.cumprimentar())  # Method Resolution Order - MRO


