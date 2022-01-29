"""
Decorators com diferentes assinaturas
# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Teste
# print(saudacao('Angelina'))
print(ordenar('Picanha', 'Batata Frita'))

# Para resoler, utilizamos um padrão de projeto chamado Decorator Patters
A assinatura de uma função é representada pelo retorno, nome e parâmetro de entrada.

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# print(saudacao('Rafael'))
print(ordenar('Picanha', 'Batata Frita'))

@gritar
def lol():
    return 'lol'
print(lol())

# OBS: Vale lembra que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

"""


# Decorators com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valores incorreto! Primeiro argumento precisa se {valor}'
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num, num2):
    return num + num2


print(soma_dez(10, 12))  # 22
