"""
Escrevendo em arquivos

# OBS: ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas eler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a fução write().
Esta função receve uma string como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita como o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
conteúdo no arquivo anterior é perdido.

"""
# Exemplo de escrita
with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Está é a última linha ')
