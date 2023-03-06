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

===========================================

* Exercício 11 - Validador de CPF

Este programa tem como objetivo validar a autenticidade de um número de CPF informado pelo usuário. O CPF é um documento de identificação muito importante no Brasil, composto por onze dígitos, sendo os dois últimos utilizados para a verificação de sua validade.

O programa utiliza um cálculo que consiste em multiplicar cada um dos nove primeiros dígitos do CPF por uma contagem regressiva iniciada em 10 e terminando em 2. O resultado da soma dessas multiplicações é multiplicado por 10 e, em seguida, dividido por 11, e o resto dessa divisão é utilizado para determinar o primeiro dígito verificador do CPF.

Para determinar o segundo dígito verificador, é utilizada uma contagem regressiva iniciada em 11 e terminando em 2, e o resultado da soma das multiplicações é multiplicado por 10 e, em seguida, dividido por 11, e o resto dessa divisão é utilizado para determinar o segundo dígito verificador do CPF.

Se os dígitos verificadores gerados pelo programa coincidirem com os dígitos verificadores informados pelo usuário, o programa informa que o CPF é válido. Caso contrário, o programa informa que o CPF é inválido.
 
