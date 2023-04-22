'''
Analise a seguinte string:

              disciplina = 'Programação III'

Qual o comando que permite verificar se a string contém caracteres não alfabéticos?

	
disciplina.char()

	
disciplina.len()

Certo		
disciplina.isalpha()

	
disciplina.alpha()

	
disciplina.strip()




Explicação:
char() ¿ não existe

len() ¿ identifica o tamanho da string.

alpha() ¿ não existe

strip() ¿ retira os espaços em branco no início e no fim da string.




 	

2.
Para ler apenas 2 caracteres de um objeto do tipo arquivo chamado arq, usamos:
	arq.readlines
	arq.open(2)
	arq.readline()
	arq.read()
Certo		arq.read(2)



Explicação: arq.read(2) é a sintaxe correta para a leitura de caracteres



 	

3.
Assinale a alternativa que crie uma tupla chamada avaliacao  com os seguintes elementos: AV, AVS, SIMULADO.

	
avaliacao {'AV', 'AVS', 'SIMULADO'}

	
avaliacao ['AV', 'AVS', 'SIMULADO']

	
avaliacao(AV, AVS, SIMULADO)

	
avaliacao [AV, AVS, SIMULADO]

Certo		
avaliacao ('AV', 'AVS', 'SIMULADO')




Explicação:
Para a criação das tuplas usamos os parênteses. Como os dados são do tipo string, os mesmos devem estar entre aspas (' ').




 	

4.
Dado o código Python abaixo, qual será a saída?

str1 = "ABCDEF"
str2 = "GHIJKL"

print(str1[:2].join(str2[3:]))

	
ABJKL

	
ABCJKL

	
DGHEGHF

	
JKLABC

Certo		
JABKABL




Explicação:
O comando join fará com que cada letra da segunda string (str2[3:] -> "JKL") seja separada pelos símbolos da primeira string(str1[:2] -> "AB")

J AB K AB L




 	

5.
Em Phyton, usamos o comando OPEN() para abrir arquivos. Quantos e quais argumentos devem ser usados no comando?

Certo		
2 argumentos, o caminho e nome do arquivo e o modo de abertura do arquivo

	
1 argumento, que é o caminho (path) do arquivo

	
nenhum argumento é necessário

	
1 argumento, o modo de abertura do arquivo

	
1 argumento, o caminho e nome do arquivo




 	

6.
Considere os seguintes comandos em Phyton

>>> str1="Phyton123"
>>> str1.isalpha()
 

Qual o resultado da execução dessas 2 linhas de código?

Certo		
false

	
Nulo

	
"123"

	
true

	
"Phyton"




 	

7.
O Python possui várias bibliotecas para manipulação de dados. Qual das opções abaixo é uma das mais utilizadas? 

Certo		
pandas

	
ursos

	
bears

	
files

	
nets




Explicação:
A biblioteca pandas do Python é uma biblioteca muito utilizada em Data Science, área que precisa manipular grande quantidade de dados.

As outras opções não se referem a bibliotecas em Python.




 	

8.
Durante o desenvolvimento de uma aplicação verificou-se a necessidade de abrir um arquivo denominado palavras.txt, mas só permitir que o usuário possa ler o arquivo. Sendo assim, qual dos comandos abaixo deve ser utilizado no Python para abrir o arquivo só para leitura e atribuir à variável temas?

Certo		
temas = open('palavras.txt', 'e')

	
temas = open('palavras.txt', 'a')

	
temas = open('palavras.txt', 'w')

	
temas = open('palavras')

	
open(temas, 'palavras.txt', 'e')

'''
