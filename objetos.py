"""
POO - Objetos

Objeto -> São instâncias da classe, ou seja, após o mapeamento do objeto do mundo real
para sua representção computacional, devemos poder criar quantos objeto forem necessários.
Podeoms pensar nos objetos/instânicas de uma classe como variáveis do tipo definido na classe.

# Instâncias ou Objetos
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_deligar()
lamp1.ligar_deligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 2000)

user = Usuario('RAFAEL', 'andreolli', 'rafaprochnow@gmail.com', '12345')

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_deligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha













