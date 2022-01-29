"""
Sorted

OBS: Não confunda, apesar do nome, com a funçaõ sort() que ja estudamos em Listas. O sort() só funciona em Listas

Podemos utilizar o sorted() com qualquer interável
Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros)) #ordenar do menor para o maior

print(numeros)
print(numeros.sort())
print(numeros)

# Adicionando alguns parâmetros ao sorted()
numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utiliar o sorted() para coisas mais complexas
print(sorted(musicas, key=lambda musica: musica['tocou']))
"""


