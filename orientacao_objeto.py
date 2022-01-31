"""
Programação Orientada aa Objeto - POO

- POO é um paradigma de programação que utiliza de mapeamente de objetos do mundo real para
modelos computacionais.

- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação Objetos
- Classe -> Modelo de objetos do mundo real sendo represenado computacionalmente;
    A partir da descrição das Classe, nós estamos no fundo definindo nosso tipo de dado
- Atributo -> Comportamento do objeto (funções);
- Construtor -> Método especial utilizado para criar os objetos;
- Objeto -> Instância da classe. Produto final;
"""

numero = 10
print(numero)
print(type(numero))

nome = 'Geek'
print(nome)
print(type(nome))


class Produto:  # Classe
    pass  # Atributos e Métodos ainda não foram definidos


ps4 = Produto()  # Contrutor
# ps4 é nosso objeto

print(ps4)
print(type(ps4))

