# Sobre os exercícios Python

Este repositório contém uma série de exercícios resolvidos em Python para demonstração de habilidades e práticas de programação que adquiri no "Curso de Python 3 do Básico Ao Avançado (com projetos reais)" ministrado pelo instrutor Luiz Otávio Miranda na plataforma Udemy. Os exercícios estão organizados em arquivos individuais.



* Exercício 1 - Variáveis e Tipos de Dados 

O objetivo deste programa é praticar a manipulação de variáveis e tipos de dados em Python, retornando informações sobre o usuário, tais como nome, sobrenome, ano de nascimento, se o usuário é maior de idade e sua altura em metros.
OBS: Para evitar informação incorreta sobre o ano de nascimento, modifiquei o programa e, com o auxílio da biblioteca datetime, calculei a idade do usuário com base na data atual. 

===========================================

* Exercício 2 - Cálculo do IMC

Neste exercício, utilizei o Python para calcular o índice de massa corporal (IMC) do usuário com base em informações como nome, altura e peso.
Este programa é útil para entender como utilizar operadores aritméticos em Python para calcular valores com base em variáveis declaradas. O cálculo do IMC também é importante para avaliar a saúde do usuário e pode ser utilizado em aplicações de saúde e fitness.

===========================================

* Exercício 3 - if e comparação 

O objetivo deste programa é comparar dois valores fornecidos pelo usuário e informar qual é o maior, o menor ou se são iguais. Para isso, são utilizados condicionais if e operadores de comparação.

===========================================

* Exercício 4 - Teste de conhecimento 

O objetivo destse programa é pedir ao usuário para digitar seu nome e idade, e com base nas informações digitadas, exibir algumas informações específicas sobre o nome informado.

===========================================

* Exercício 5 (triplo) - Condições

*Exercício 5.1: verifica se um número é par ou ímpar.

*Exercício 5.2: retorna uma saudação baseada na hora do dia fornecida pelo usuário.

*Exercício 5.3: classifica o tamanho de um nome em pequeno, normal e grande.

===========================================

* Exercício 6 - Iterando Strings com while

O objetivo deste programa é solicitar ao usuário que digite o seu nome e, em seguida, iterar sobre as letras do nome
para criar uma nova string com asteriscos entre as letras. Por fim, adicionar um asterisco no final.

===========================================

* Exercício 7 - Calculadora Python

Este programa é um exemplo de uma calculadora com loop while que permite que o usuário execute várias operações até que decida sair.
OBS: Acrescentei o método .is_integer() na linha 48 para evitar a exibição de um valor decimal no resultado quando os dois números escolhidos pelo usuário forem inteiros.

===========================================

* Exercício 8 - Jogo da Forca

O jogo da forca é um jogo popular em que um jogador deve adivinhar uma palavra secreta, letra por letra, antes de atingir o número máximo de tentativas e ser "enforcado". Nesta versão do jogo, o usuário vai tentar adivinhar uma palavra aleatória de uma lista de palavras possíveis que estabeleci.
 OBS: Para ficar mais intuitivo, utilizei o módulo "random" para selecionar uma palavra aleatória da lista. Também fiz com que o programa transforme a palavra em uma lista de caracteres e crie uma lista com as letras adivinhadas, representadas por "_".
 
 ===========================================
 
 * Exercício 9 - índices de lista
 
 O objetivo deste programa é exibir os índices de uma lista.
 
 ===========================================
 
 * Exercício 10 - Lista de Compras
 
O programa é uma ista de compras onde o usuário tem a possibilidade de inserir, apagar e listar valores da sua lista de modo prático.

============================================

* Exercício 11 - Validador de CPF

Este programa tem como objetivo validar a autenticidade de um número de CPF informado pelo usuário. O CPF é um documento de identificação muito importante no país, composto por onze dígitos, sendo os dois últimos utilizados para a verificação de sua validade.

O programa utiliza um cálculo que consiste em multiplicar cada um dos nove primeiros dígitos do CPF por uma contagem regressiva iniciada em 10 e terminando em 2. O resultado da soma dessas multiplicações é multiplicado por 10 e, em seguida, dividido por 11, e o resto dessa divisão é utilizado para determinar o primeiro dígito verificador do CPF.

Para determinar o segundo dígito verificador, é utilizada uma contagem regressiva iniciada em 11 e terminando em 2, e o resultado da soma das multiplicações é multiplicado por 10 e, em seguida, dividido por 11, e o resto dessa divisão é utilizado para determinar o segundo dígito verificador do CPF.

Se os dígitos verificadores gerados pelo programa coincidirem com os dígitos verificadores informados pelo usuário, o programa informa que o CPF é válido. Caso contrário, o programa informa que o CPF é inválido.
 
 ============================================
 
 * Exercício 12 - Exercício com Funções
 
Este código define duas funções e as utiliza para demonstrar o uso de parâmetros de posição, operadores matemáticos e condicionais.

A primeira função, chamada "multiplicar", utiliza um parâmetro de posição *args para receber um número variável de argumentos, multiplica todos eles juntos e retorna o resultado. Em seguida, a função é chamada com três argumentos e o resultado é impresso na tela.
A segunda função, chamada "par_impar", recebe um argumento inteiro "numero" e retorna True se o número é par e False caso contrário. Em seguida, a função é chamada com quatro valores diferentes e os resultados são impressos na tela.
A terceira função, chamada "par_impar2", é uma variação da segunda função que, ao invés de retornar True ou False, retorna uma string indicando se o número é par ou ímpar. 

 ============================================
 
 * Exercício 13 - Função duplicadora, triplicadora e quadriplicadora
 
Este código define três funções que recebem um número como parâmetro e retornam o resultado da multiplicação desse número. Essas funções são chamadas duplicar(), triplicar() e quadruplicar(). Em seguida, cada função é chamada com um exemplo de número para demonstrar seu funcionamento. Esse código pode ser utilizado em projetos que precisam de funções para realizar a duplicação, triplicação ou quadruplicação de um número.

============================================

* Exercício 14 - Sistema de perguntas e respostas

Este programa cria um sistema de perguntas e respostas. Ele armazena cada pergunta, opções e a resposta correta em um dicionário, e depois apresenta cada pergunta para o usuário com as opções de resposta correspondentes. O usuário pode escolher uma das opções apresentadas digitando o índice correspondente, e o programa verifica se a resposta está correta ou não. No final, ele exibe a quantidade de respostas corretas que o usuário acertou e quantas perguntas haviam no total. O objetivo do código é testar o conhecimento do usuário em relação às perguntas apresentadas.

============================================

* Exercício 15 - Encontrando o primeiro número duplicado em uma lista de inteiros

Este código define uma função chamada "encontra_primeiro_duplicado" que recebe uma lista de números inteiros e retorna o primeiro número duplicado na lista (considerando a segunda ocorrência como a duplicação). Se não houver duplicados na lista, a função retorna -1.

Em seguida, o código define uma lista de listas de números inteiros chamada "lista_de_listas_de_inteiros" e itera sobre ela, imprimindo cada lista seguida do primeiro número duplicado encontrado na lista, usando a função "encontra_primeiro_duplicado".

============================================

* Exercício 16 - Ordenação e deep copy de lista de dicionários de produtos

Este código aumenta o preço de uma lista de produtos em 10%, gera cópias profundas da lista original, ordena a lista de produtos por nome em ordem decrescente e depois por preço em ordem crescente, gerando novas cópias profundas para cada uma dessas listas ordenadas. Por fim, o código imprime as listas ordenadas por nome e por preço.

============================================

* Exercício 17 - Criação de closures

O código permite que funções sejam criadas de forma dinâmica e adiada, permitindo que seus parâmetros sejam especificados em um momento posterior, é o chamado 'closure' de funções.

============================================

* Exercício 18 - zip / zip_longest

Este código tem como objetivo praticar o uso da função zip ou zip_longest para unir duas listas na ordem. A ideia é que a função "zipper" possa usar todos os valores da menor lista e juntá-los em tuplas com os valores correspondentes da outra lista. O código apresenta dois exemplos de como utilizar as funções zip e zip_longest para atingir esse objetivo, demonstrando suas diferenças e vantagens em diferentes situações. 

============================================

* Exercício 19 - Somando Listas

A função recebe duas listas de inteiros ou floats e retorna uma nova lista com os valores somados em pares, elemento a elemento. Caso uma lista seja maior que a outra, apenas os elementos até o tamanho da menor lista serão considerados na soma. Fiz uso da função zip() para iterar simultaneamente sobre as duas listas, somando os elementos em cada par. Caso as listas tenham tamanhos diferentes, pode-se utilizar a função zip_longest() para preencher com um valor padrão (por padrão, None) os elementos faltantes de qualquer uma das sequências. A solução apresentada usa a função zip() em conjunto com list comprehension para gerar a nova lista com os valores somados. Também é apresentada uma solução alternativa que utiliza um loop for para percorrer as listas e somar os valores em cada posição, gerando a nova lista com os resultados.

============================================

* Exercício 20 - Lista TODO com desfazer e refazer

Este programa é uma lista de tarefas que permite o usuário adicionar, listar, desfazer e refazer tarefas. As tarefas adicionadas são armazenadas em uma lista todo, enquanto as tarefas desfeitas são armazenadas em uma lista undo e as refeitas em uma lista redo. O programa também usa o módulo 'os' para limpar a tela do console após cada comando, e o módulo json para salvar as tarefas em um arquivo tasks.json. O usuário pode sair do programa digitando "sair", o que exclui o arquivo tasks.json.

============================================

* Exercício 21 - Salvando instâncias de classes em .json

Este código tem o objetivo proposto de salvar as instâncias de uma classe em arquivos JSON e, em seguida, recuperá-las desses arquivos. O código cria uma lista de instâncias da classe ComputerSell e salva cada instância em um arquivo JSON separado usando um loop for. Em seguida, o código lê cada arquivo JSON e cria uma nova instância da classe com base nos dados do arquivo.

============================================

* Exercício 22 - Exercício com classes

Este código apresenta uma implementação básica de classes relacionadas a carros, motores e fabricantes. Ele demonstra como essas classes podem ser interligadas para representar a relação entre eles.

============================================

* Exercício 23 - Banco com Abstração, Herança, Encapsulamento e Polimorfismo

Sistema bancário simples utilizando classes juntamente com os pilares da Programação Orientada a Objetos. Faça alterações em main.py e execute-o para testar diferentes atributos e valores.

============================================

* Exercício 24 - Informações de parcelamento com os módulos datetime e dateutil

Esse código é um exemplo de como calcular e printar parcelas de um empréstimo em um determinado período de tempo. 

OBS:. Para testar, crie um ambiente virtual estando na pasta raiz dos exercícios:

<code>python -m venv venv</code>

Depois ative-o:

<code>.\nome_da_virtualenv\Scripts\activate</code> (Windows)

<code>source nome_da_virtualenv/bin/activate</code> (Linux ou macOS)

Instale os requisitos:

<code>pip install -r requirements.txt</code>