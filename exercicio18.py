# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest # zip_longest é uma alternativa ao zip() que permite unir duas ou mais sequências, 
                                  # preenchendo com um valor padrão (por padrão, None) os elementos faltantes 
                                  # de qualquer uma das sequências.

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ', 'AM']

cidades_estados = list(zip(cidades, estados))
cidades_estados_2 = list(zip_longest(cidades, estados, fillvalue='Não existe'))

print(cidades_estados)
print(cidades_estados_2)