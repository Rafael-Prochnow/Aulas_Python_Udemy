"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.

"""


# Problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        """ Eu sou uma função de logar dentro de outra"""
        print(f'Você está chamando{funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b
