"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem de execução dos métodos
(Quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos Métodos (MRO) de três formas:
    - Via propriedade de classe __mro__
    - Via método mro()
    - Via help

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

    def cumprimentar(self):
        return f'Pinguim'


rafa = Pinguim('Rafa')
print(rafa.cumprimentar())  # Method Resolution Order - MRO

"""
Pinguim(Aquatico, Terrestre)
Eu sou Rafa do mar

Pinguim(Terrestre, Aquatico)
Eu sou Rafa da Terra
"""

# from mro import Pinguim

# Pinguim.__mro__

# print(Pinguim.mro())

print(help(Pinguim))
