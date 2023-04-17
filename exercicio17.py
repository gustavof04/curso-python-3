# Exercício - Adiando execução de funções
# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

# Código solucionado
def soma_com_valor(valor):
    def soma(x):
        return x + valor
    return soma

def multiplica_por_valor(valor):
    def multiplica(x):
        return x * valor
    return multiplica

soma_com_cinco = soma_com_valor(5)
multiplica_por_dez = multiplica_por_valor(10)

print(soma_com_cinco(10))
print(multiplica_por_dez(4))