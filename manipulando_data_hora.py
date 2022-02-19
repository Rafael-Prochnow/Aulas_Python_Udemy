"""
Manipulando data e hora
Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime

print(datetime.datetime.now())

# datetime.datetime(year, moth, day, hour, minite, second, microsecond)
print(repr(datetime.datetime.now()))

inicio = datetime.datetime.now()

# Alterar o horário para 16h, 0 minutos, 0 segundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

evento = datetime.datetime(2019, 1, 1, 0)

# print(evento)

# Transformando str para datetime
nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')


nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
print(type(nascimento))
"""
import datetime

evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.minute)
# Só estou fazendo isso por motivos importantes

