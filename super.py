"""
POO - Método Super()

O método super() se refere á super classe

"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especiae = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        self.__raca = raca


felix = Gato('Felilz', 'Felino', 'Angorá')
felix.faz_som('miau')
