"""
Manipulando data e hora
Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime
"""

import datetime

print(datetime.datetime.now())

# datetime.datetime(year, moth, day, hour, minite, second, microsecond)
print(repr(datetime.datetime.now()))

inicio = datetime.datetime.now()

# Alterar o horário para 16h, 0 minutos, 0 segundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

