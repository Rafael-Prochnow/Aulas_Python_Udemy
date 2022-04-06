"""
Trabalhando com delta (diferença) de data e horas

data_inicial = dd/mm/yyyy 12:55:34.987674
data_final = dd/mm/yyyy 13:34:23.987674

delta = data_final-data_inicial


# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2023, 3, 3, 0)

tempo_para_evento = aniversario - data_hoje
print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas ')
"""

import datetime
# Temos a data da compra
data_da_compra = datetime.datetime.now()
print(data_da_compra)
regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)




