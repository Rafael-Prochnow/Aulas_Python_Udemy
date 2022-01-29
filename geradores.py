"""
Geradores
- Geradores (Generators) são Iteradores (Iteradores)
# OBS: O contrário não é verdadeiro, ou seja, nem todo interator é generator

Outras informações?
- Generators podem ser criadas com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

---------------------------------------------------------------------------------
| Funções                              |  Generator Function                     |
---------------------------------------------------------------------------------
| utilizam return                      |  Utilizam yield                         |
---------------------------------------------------------------------------------
| Retorna uma vez                      |  Podemos Utilizar yield multiplas vezes |
---------------------------------------------------------------------------------
| Quando executada, retorna um valor   | Quando executada, retorna um Generator  |
---------------------------------------------------------------------------------
gen = conta_ate(10)
for num in gen:
    print(num)

gen = conta_ate(5)
# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

# Exemplo de Função Geradora (Generator funcion)
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Um GENERATOR Function nã é um Generator. Ela gera um Generator;

gen = list(conta_ate(10))
print(gen)

