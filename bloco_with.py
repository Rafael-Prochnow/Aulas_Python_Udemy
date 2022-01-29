"""
O bloco With
Passo para se trabalhar com arquivos

1º abrimos o arquivo com open()
2º Manipulamos o arquivo com read()
3º Fechamos o arquivo com close()

O cloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with

# O block with é a forma pythônica de manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.read())

# Quando saimos desse contexto, o aquivo está fechado
"""

arquivo= open('texto.txt', encoding='UTF-8')
print(arquivo)
print(type(arquivo))
print(arquivo.read())