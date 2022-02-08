"""
POO - Polimorfismo

Poli -> Muitas
Morfismo -> Formas

Quando implementamos um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método (Overrinding)

O overriding é a melhor representação do polimorfismo

"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        # Estamos gerando um método específico e se caso não seja ativado, aparece uma exceção
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.nome} está comendo ...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} falar wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala algo ...')


# Teste
felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
