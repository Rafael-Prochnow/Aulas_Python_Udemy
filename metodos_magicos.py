"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam o dunder (Double Underscore)

dunder init -> __init__  # Método Construtor
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


dunder repr -> __repr__  # Utilizado para representar o objeto e gera output para o desenvolvedor
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'


dunder str -> __str__  # Utilizado para representar o objeto legível e gera output para o usuário final
# OBS: __str__ TEM PREFERENCIA NA ATIVAÇÃO
    def __str__(self):
        return self.titulo

dunder len -> __len__  # Utilizado para contar o tamanho da vaiável inteira
    def __len__(self):
        return self.paginas

dunder del -> __del__  # Utilizado para deleter vaiáveis da memória
    def __del__(self):
        print('um Objeto do tipo Livro foi deletado da memória')


dunder add -> __add__  # Utilizado para acrescentar dois objetos
    def __add__(self, other):
        return f'{self} - {other}'

"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('um Objeto do tipo Livro foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += '' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(len(livro2))

print(livro1 * 3)
