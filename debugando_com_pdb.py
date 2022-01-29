"""
Debugando com PDB
PDB -> Python Debugger

1º maneira de achar os bugs é utilizando os prints
# A utilização dos prints para debugar código é uma prática ruim,
# já que existem forams mais profissionais de ser fazer isso, como utilizar o debugger

2º utilizando o PDB 

def dividir(a,b):
    try:
        return int(a)/ int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4,0))
"""


