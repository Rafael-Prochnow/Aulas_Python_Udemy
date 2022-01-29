"""
Modos de Abertura de Arquivo

r -> Abre para leitura - Padrão
w -> Abre para escrita - Sobrescreve o arquivo já existente
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FiliExistesError
a -> Abre para escrita, adicionando o contuúdo ao final do arquivo.
# OBS: Abrindo o modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado ao final.
'+' -> Abre o modo de atualização: Leitura e Escrita. 

# Exemplo x

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já Existe!')



"""
