"""
POO - Métodos

Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações que este objeto
pode realizar no seu sistema.

Em Python dividimos os métododos em 2 grupos: Método de instância e Método de classe.

# Método de intânica
# O método dunder init __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

OBS: Os elementos em python que inicia e finaliza com duplo underline é chamdo de dunder (Double Underline)

OBS: Os métodos/função dunder em python são chamado de métodos mágicos

ATENÇÃO: Por mais que podemos criar nossas funções utilizando dunder, não é
aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o
comportamento dessas funções mágicas internas da linguagem. Então evite ao máximo. De preferência
nunca faça isso.

# Exemplo

    def __correr__(self, metros):
        print(f'{self.__name} está correndo {metros} metros')

# Métodos são escritos em letras minúsculas. Se o nome for composo, o nome terá as
palavras separadas por underline.

p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(50))

user1 = Usuario('Angela', 'Jolie', 'angelina@gmail.com', '12345')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '67891')

print(user1.nome_completo())
print(user2.nome_completo())

print(f'Senha User 1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe
print(f'Senha User 2: {user2._Usuario__senha}')  # Acesso de forma errada de um atributo de classe


"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor da produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, round=200000, salt_size=16)

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('informe o nome: ')
sobrenome = input('informe o sobrenome: ')
email = input('informe o email: ')
senha = input('informe o senha: ')
confirma_senha = input('Conferir a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')

senha = input('infrme a senha para acessso')

