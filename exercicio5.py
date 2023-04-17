"""
Exercício triplo sobre condições

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
while True:
    entrada = input('Digite um número inteiro: ')
    if entrada.isdigit():
         entrada_int = int(entrada)
         par_impar = entrada_int % 2 == 0
         par_impar_texto = 'ímpar'

         if par_impar:
             par_impar_texto = 'par'

         print(f'O número {entrada_int} é {par_impar_texto}')
         break
    else:
         print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
while True:
    question_hours = input('Que horas são? ')
    if len(question_hours) == 5 and \
        question_hours[2] == ':' and \
        question_hours[:2].isnumeric() and \
        question_hours[3:].isnumeric():
            hours = int(question_hours[:2])
            minutes = int(question_hours[3:])
            if hours >= 0 and hours <= 23 \
                and minutes >= 0 and minutes <= 59:
                    if question_hours >= '00:00' and question_hours <= '11:59':
                        print('Bom dia!')
                    elif question_hours >= '12:00' and question_hours <= '17:59':
                        print('Boa tarde!')
                    else:
                        print('Boa noite!')
                    break
            else:
                print('Horário inválido. Digite um horário entre 00:00 e 23:59.')
    else:
        print('Formato de hora inválido. Use o seguinte formato: XX:XX')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é grande". 
"""
while True:
    nome = input('Digite seu primeiro nome: ')
    tamanho = len(nome)

    if tamanho <= 4:
        print('Seu nome é curto.')
    elif 5 <= tamanho <= 6:
        print('Seu nome é normal.')
    elif 7 <= tamanho <= 11:
        print('Seu nome é grande.')
    else:
        print('Nome inválido para consulta.')
    if not nome:
        print('Você não digitou nenhum nome.')
        continue
    break