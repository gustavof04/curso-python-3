# Exercício - Calculadora com while
import os
import platform

print('Bem-vindo à calculadora Python!')
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Escolha um operador (+, -, *, /): ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta, confira o resultado abaixo:')
    if operador == '+':
        resultado = num1_float + num2_float
    elif operador == '-':
        resultado = num1_float - num2_float
    elif operador == '*':
        resultado = num1_float * num2_float
    elif operador == '/':
        resultado = num1_float / num2_float
    else:
        resultado = None

    if resultado is None:
        print('Nunca deveria chegar aqui.')
    elif num1_float.is_integer() and num2_float.is_integer():
        print(int(resultado))
    else:
        print(resultado)

    sair = input('Quer sair? [s]im ou [n]ão: ').lower()

    if sair.startswith('s'):
        print('Você saiu da calculadora.')
        break
    elif sair.startswith('n'):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print('Você optou por ficar!')
        continue
    else: 
        print('Opção Inválida. Saindo da calculadora.')
        break