"""
POO - Atributo

Atributos -> Representam as características do objeto, ou seja, pelos atributos nós
conseguimos representar computacionalmente os estados de um objeto

Em Python, dividimos os atributos em 3 grupos:
    - Instâncias
    - Classes
    - Dinâmicos

# Atributo de instâncias: São atributos declarados dentro do método construtor

OBS: Método construto: É um método especial utilizado para a construção do objeto

# Em Java, uma classe Lâmpada, incluindo seus atibutos ficaria mais ou menos:

puclic class Lampada(){    #  Classe
    private int voltagem;    # Declarar as variáveis
    puclic String cor;
    protected Boolean ligada = False;

    puclic Lambada(int voltagem, String cor){    # CONSTRUTOR
        this.voltagem = voltagem;
        this.cor = cor
    {
}

# Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é Público,
ou seja, pode ser acessado em todo projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declada, utiliza-se
__ duplo underscore no início do seu nome. Isso é conhecido também como Name Manling

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# Vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo
# user é uma instância da classe Acesso
user = Acesso('user@gmail.com', '123456')

print(user.email)
# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso, mas não deveríamos fazer este acesso (Name Mangling)
# Acessar ao atributo dentro da própria classe
user.mostr_senha()

# Atributos de Instâncias
# Significa que ao criarmos intâncias/objetos de uma classe, todas as instâncias terão estes atributos
user1 = Acesso('user1@gmail.com', '12345')
user2 = Acesso('user2@gmail.com', '56789')

user1.mostra_email()
user2.mostra_email()

# Atributos de classes, são atrivutos que são declarados diretamente na classe, ou seja,
# fora do construtur. Geralmente já inicializamos um valor e este valor é compratilhado entre
# Todas as instânicas da classe. Ou seja, ao invés de cada instãncia da classe ter seus próprios valores
# como é o caso dos atributos de instâncias, com os atributos de classe todas as intâncias
# terão o mesmo valor para este atributo

p1 = Produto('PlayStation 4', 'Vido Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagem como Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos


"""


# Classe com Atributos de Instância Público
class Lampada:  # Classe
    def __init__(self, voltagem, cor):  # __init__ é nosso Método Construtor
        self.voltagem = voltagem  # Atributo voltagem
        self.cor = cor  # Atributo cor
        self.ligada = False  # Atributo ligada


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero  # o Atributo numero do objeto Lampada vai receber numero
        self.limite = limite  # O Atributo limite do objeto Lampada vai receber limite
        self.saldo = saldo  # O Atributo saldo do objeto Lampada vai receber saldo


# Self é (auto-serviço) objeto que está executando o Método
# ps4 = Produto()  # Método __init__ sendo executado
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Class de acesso Privadado
# __ significa que a variável criada é privada e apenas a classe tem acesso
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostr_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos de Classe
class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # Atributo de Instânicas
        self.nome = nome  # Atributo de Instânicas
        self.descricao = descricao  # Atributo de Instânicas
        self.valor = (valor * Produto.imposto)  # Atributo de Instânicas
        Produto.contador = self.id  # Atributo de Classe


# Atributo Dinâmico -> Um atributo de instânica que pode ser criado em tempo de execução.
# OBS: O atributo dinâmico será exclusivo da instânica que o criou
p1 = Produto('PlayStation 4', 'Vido Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Criando um atributo dinâmico em tempo de exeução
p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso
# print(f'Produto: {p2.nome}, Descição: {p2.descricao}, Valor: {p2.valor}, peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descição: {p1.descricao}, Valor: {p1.valor}, peso: {p1.peso}')

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)


