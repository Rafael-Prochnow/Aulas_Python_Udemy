"""
Aistema de Arquivos e Navegações

Para fazer uso de manipulação de arquivos do sitema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# Verificar o diretório corrente -> getcwd: pega o current work directory (diretório de trabalho corrente)
# Retorna o Path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
# OBS: Se você estiver utilizando um computador com Windows,
# Terá que ter cuidado ao verificar o diretório
print(os.path.isabs(('C:\\Users\\Rafael\\PycharmProjects\\Udemy'))) # True

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

import sys
# Podemos ter mais detalhes no sistema operacional
print(sys.platform)

print(os.getcwd())
res = os.path.join(os.getcwd(), 'geek')

os.chdir(res)
print(os.getcwd())

# Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretório atual e o segundo o
# Diretório que será juntado ao atual

# Podemos listar os arquios e diretórios com o listdir()
print(os.listdir())
"""
import os



