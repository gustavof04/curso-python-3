import copy
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

for produto in produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

novos_produtos = copy.deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
produtos_ordenados = sorted(novos_produtos, key=lambda n: n['nome'], reverse=True)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(produtos_ordenados)

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados = sorted(novos_produtos, key=lambda p: p['preco'])

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados)

print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')