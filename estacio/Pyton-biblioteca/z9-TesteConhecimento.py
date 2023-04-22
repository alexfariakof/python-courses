Para utilizarmos em Python funções matemáticas como por exemplo math.sqrt(2) precisamos em primeiro lugar carregar um módulo. Qual das instruções abaixo realiza essa situação?

	
import all math functions 

	
Math.load math

	
load math package 

Certo		
import math 

	
Math.math




Explicação:
Em Python utilizamos o comando ¿import¿ para carregar um módulo, no caso acima a intrução para carregar o módulo math seria ¿import math¿.




 	

2.
Considere o seguinte código em Python. É uma função que retorna mais de um valor.

def sp(x,y):

  return (x+y),(x*y)

Qual estrutura de dados está permitindo esse retorno no código acima?

	
string

	
lista

Certo		
tupla

	
array

	
vetor




Explicação:
A estrutura que permite é a tupla. A função sp() está retornando uma tupla com elementos de soma e produto. 




 	

3.
Para o seguinte código abaixo um tipo de dados não pode ser utilizado, qual?

def f(l):

  for i in l:

    print(i)

	
dicionário

	
lista

	
string

Certo		
inteiro

	
tupla




Explicação:
A função definida itera sobre um tipo de dados que possua vários componentes, no caso lista, tupla e string podem ser utilizadas com a função, mas se for usado o tipo inteiro ocorrerá um erro. A resposta correta é inteiro.




 	

4.
Em Phyton, tal qual em outras linguagens de programação, esperamos que uma funçao retorne um valor. E para tal usamos a palavra chave ________. Porém nem sempre essa palavra chave é obrigatória. Em algumas linguagens, quando isso ocorre a função é chamada de __________________

Assinale a UNICA opção que completa as frases adequadamente.

Certo		
return e procedure (procedimento)

	
Result e rotina em geral

	
Value e procedure (procedimento)

	
Target e procedure (procedimento)

	
Enter e procedure (procedimento)




 	

5.
Considere o trecho de código a seguir, em Phyton

def maior(a, b):
     if a > b:
          print(a, 'é o maior')
     elif a == b:
          print(a, 'é igual a', b)
     else:
          print(b, 'é o maior')

maior(4, 1)

assinale a correta saída do trecho de código

	
1 é o maior

	
o trecho de código não executa

Certo		
4 é o maior

	
nulo

	
4 é igual a 1




Explicação:
a = 4 

b = 1

a > b --> 4 ´é o maior




 	

6.
Avalie cada assertiva a seguir no que se refere a aplicação dos conceitos de escopo e tempo de vida de uma variável

I. Não é possível  ter uma variável local a uma função com mesmo nome de uma variável global

II. Uma variável local só é reconhecida enquanto a função estiver em execução

III. A forma de defirmos em Phyton que uma variável usada internamente em uma função é na verdade global, é inserir o termo global antes da referencia a variável, dentro da função. Algo  como  global ind, sendo "ind" o nome da variável global.

Assinale a Unica opção que apresenta a resposta com as assertvas corretas

	
Apenas III

	
Apenas I e II

	
Apenas II

Certo		
Apenas II e III

	
I, II e III




Explicação:
I. Não é possível  ter uma variável local a uma função com mesmo nome de uma variável global - FALSO, é possível sim

II. Uma variável local só é reconhecida enquanto a função estiver em execução --> VERDADE

III. A forma de defirmos em Phyton que uma variável usada internamente em uma função é na verdade global, é inserir o termo global antes da referencia a variável, dentro da função. Algo  como  global ind, sendo "ind" o nome da variável global. -->VERDADE

