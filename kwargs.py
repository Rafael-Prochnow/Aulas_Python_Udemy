"""
Poderiamos chamar esse parãmetro de **xis, mas por converção chamamo de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwrags exige que utilizemos parâmetros nomeados, e trasforma esses
parâmetros extras em um dicionário.


# Exemplo
def cores_fovoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_fovoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e *kwargs não são obrigatórios

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek'
    return 'Não tem certeza quem você é ..;'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

# Nas nossa funções, podemos ter (nessa ordem):
- Parâmetros obrigatórios
- *args
- Patâmetros default (Não obrigatórios)
- **kwargs

# Desempacotar com **kwargs

def mostrar_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome' : 'Falicity', 'sobrenome' : 'Jones'}

print(mostrar_nomes(nome='Falicity', sobrenome='Jones'))
print(mostrar_nomes(**nomes))

"""

# Outro exemplo

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS: Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros da função
# dicionario = dict(d=1, e=2, f=3)  # TypeErros
# soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, name='OLÁ')

