"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?
- Quando um linguagem de programação suporta HOF indica que podemos ter funções que retornam outras
funções como resultado ou mesmo que podemos passar funções como argumentos para outras
funções e até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, Fist Class Citizem

# Exemplos - Definindo as funções
def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as fumções
print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funções Alinhadas
Em Python podemos ter Funções dentro de Funções, que são conhecidas por Nested Functions
ou também conhecidas como Inner Functions (Funções Internas)

# Exemplo
from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui', 'Gosto muito de você'))
    return humor() + pessoa

print(cumprimento('Angelina'))

print(cumprimento('Felicity'))
"""


