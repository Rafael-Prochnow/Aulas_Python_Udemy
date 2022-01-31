"""
POO- Classes

Em POO Classes são modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos: Representam as caratcterísticas do objeto, ou seja, pelos atributos
    conseguimos representar computacionamente os estados de um objeto. No caso da Lâmpada,
    possivelmente iríamos querer saber se a lâmpada é 110 ou 220 voltz, se ela é branca, amarela,
    vermelha ou outra cor, qual a luminosidade dela e etc.

    - Métodos (Funções): Representam os comportamento dos objetos, ou seja, as ações qeu este objeto
    poderealizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito
    provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em Python para definiar uma classe utilizamos a palavra reservada class

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome inicial em
Maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em Maiúsculo, todas juntas.

OBS: Quando estamos planejanto um sofware e difinimos quias classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade.

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, deretório e etc.
"""


# Criando um tipo de dado
class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


valor = int('42')  # cast, int nada mais é do que uma classe em Python

