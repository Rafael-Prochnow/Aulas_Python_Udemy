"""
Escrevendo um iterador Customizado

# Ideia utilizada
for n in range(11):
    print(n)

"""
class Contador:
    def __init__(self, menor, maior): # __init__ função especial chamada de construtor, criando objetos
        self.menor = menor
        self.maior= maior
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


# con = Contador(1, 61)
for n in Contador(1, 10):
    print(n)

