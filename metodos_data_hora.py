"""
Métodos de Data e Hora

agora = datetime.datetime.now()
print(agora)
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(repr(hoje))

# Mudanã ocorrendo à meia-noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana. weekday()
# Os dias da semana do método weekyday() começam em 0, sendo está a segunda-feira

# 0 - Segunda feira (Monday)
# 1 - Terça-Feira (Tuesday)
# 2 - Quarta-Feira (Wednesday)
# 3 - Quinta-Feira (Thursday)
# 4 - Sexta-Feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nascesceu em uma Segunda-Feira')
elif aniversario.weekday() == 1:
    print('Você nascesceu em uma Terça-Feira')
elif aniversario.weekday() == 2:
    print('Você nascesceu em uma Quarta-Feira')
elif aniversario.weekday() == 3:
    print('Você nascesceu em uma Quinta-Feira')
elif aniversario.weekday() == 4:
    print('Você nascesceu em uma Sexta-Feira')
elif aniversario.weekday() == 5:
    print('Você nascesceu em uma Sábado')
elif aniversario.weekday() == 6:
    print('Você nascesceu em uma Domingo')

# Formatando data/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

"""
import datetime
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime(''))}"




