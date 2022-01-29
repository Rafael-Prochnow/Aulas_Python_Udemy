"""
Decoradores (Decorators)

O que são Decorators?
- Decorators são funções;
- Decorators envolvem outras funções que aprimoram seus comportamentos
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sitaxa própria, usando "@" (Syntact Sugar / Açúcar Sintático)

|--------------------------------------------|
|         Function Decorator                 |
|--------------------------------------------|

|--------------------------------------------|
|          Função Decorada                   |
|--------------------------------------------|

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo hahahah')

# Teste 1
teste = seja_educado(saudacao)
teste()

# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando
apresentando()

"""
"""
|--------------------------------------------------------|
|  Home   |   Serviços    |   Produtos  | Administrativo |
|--------------------------------------------------------|

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/serviços
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

# OBS: Não é um código funcional. É apenas um exemplo

def checa_loging (request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br'

def home(request):
    return 'Pode acessar home'
    
def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_loging
def admin(request):
    return 'Pode acessar admin'
ola
"""


