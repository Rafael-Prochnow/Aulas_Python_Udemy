"""
StrigIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacicnal o software precisa ter permissão:
    - Permissão de Leitura
    - Permissão para Escrever
StringIO -> Utilizado para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO
mensagem = 'Esta é apenas um string normal'

# Podemos criar um arquivo em memória já como uma string inserida ou mesmo vazia para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilziar tudo que já sabemos
print(arquivo.read())

# Escrever outros textos
arquivo.write(' Outro texto')

# Podemos incllusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())



