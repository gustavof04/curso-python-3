import random
# Exercício - Jogo da Forca 
# (modificado por mim com o objetivo de ficar  
# mais intuitivo e desafiador para o usuário)

print ('Bem-vindo(a) ao jogo da forca!')

# Lista de palavras possíveis
palavras = ['PROJETO', 'PYTHON', 'PROGRAMACAO', 'COMPUTADOR', 'JOGO']

# Escolhendo uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

# Transformando a palavra em uma lista de caracteres
palavra_secreta = list(palavra_secreta)

# Criando a lista com as letras adivinhadas
palavra_adivinhada = ["_" for i in range(len(palavra_secreta))]

# Contador de tentativas
tentativas = 0

# Loop principal do jogo
while "_" in palavra_adivinhada and tentativas < len(palavra_secreta):
    letra = input('Digite uma letra: ')
    if not letra.isupper():
        print('Por favor, digite uma letra maiúscula.')
        continue
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_adivinhada[i] = letra
        print(''.join(palavra_adivinhada))
    else:
        tentativas += 1
        print('*')
if "_" not in palavra_adivinhada:
    print('Parabéns, você escapou da forca!')
else:
    print('Você foi enforcado, a palavra era', ''.join(palavra_secreta))
print(f'Você errou', tentativas, 'vezes.')