# Crie uma função que multiplica todos os
# argumentos não nomeados (posicionais) recebidos
# Retorne o total para uma variável e mostre
# o valor da variável.
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplication = multiplicar(54, 4, 23)
print(multiplication)

# Crie uma função que fala se o número é par ou ímpar
# Retorne se o número é par ou ímpar. (True = Par, False = Ímpar)
def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(3))
print(par_impar(321))
print(par_impar(40))

#OU

def par_impar2(numero2):
    multiplo_de_dois = numero2 % 2 == 0

    if multiplo_de_dois:
        return f'{numero2} é par'
    return f'{numero2} é ímpar'

print(par_impar2(2))
print(par_impar2(34))
print(par_impar2(57))
print(par_impar2(432))
print(par_impar2(0))