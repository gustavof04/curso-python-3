# Exercício com variáveis e tipos de dados

# Informações do usuário
nome = 'Gustavo'
sobrenome = 'Fernandes'
ano_nascimento = 2004
dia_nascimento = 29
mes_nascimento = 10

# Ano de nascimento (calculando a idade com base na data atual)
from datetime import date
hoje = date.today()
idade = hoje.year - ano_nascimento - ((hoje.month, hoje.day) < (mes_nascimento, dia_nascimento))

# Demais informações
maior_de_idade = idade >= 18
altura_metros = 1.71

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('Maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)