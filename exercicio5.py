"""
Exercício triplo sobre condições

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')
if entrada.isdigit():
     entrada_int = int(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
else:
     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
question_hours = input('Que horas são? ')
if question_hours >= '00:00' and question_hours <= '11:59':
    print('Bom dia!')
elif question_hours >= '12:00' and question_hours <= '17:59':
    print('Boa tarde!')
elif question_hours >= '18:00' and question_hours <= '23:59':
    print('Boa noite!')

    if question_hours == int:
        print('Formato de hora inválido. Use o seguinte formato: XX:XX')    

else:
    print('Formato de hora inválido. Use o seguinte formato: XX:XX')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é grande". 
"""
nome = input('Digite seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é curto.') 
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal.')
elif len(nome) > 6 and len(nome) < 12:
    print('Seu nome é grande.')
elif len(nome) >= 12:
    print('Nome inválido para consulta.')