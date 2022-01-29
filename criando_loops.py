"""
Criando sua própria versão de loop
for num in [1, 2, 4, 5, 6]:
    print(num)

for letra in 'Geek':
    print(letra)

"""
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Geek university')
