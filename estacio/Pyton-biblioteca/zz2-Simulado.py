'''
A linguagem Python é relativamente nova, lançada em 1991. É uma linguagem de uso geral, projetada especificamente para tornar os programas bastante legíveis.  São características da linguagem:

	
Tipagem Dinâmica, suporta o paradigma de programação funcional, é uma linguagem compilada.

 Certo	
Tipagem Dinâmica, suporta o paradigma de programação funcional, é uma linguagem interpretada.

	
Tipagem não Dinâmica, suporta o paradigma de programação funcional, é uma linguagem compilada.

	
Tipagem não dinâmica, suporta o paradigma de programação funcional, é uma linguagem interpretada.

	
Tipagem Dinâmica, suporta o paradigma de programação lógica, é uma linguagem compilada.

Respondido em 21/03/2023 02:25:00


Explicação:
A linguagem Python é multiparadigma, ou seja trabalha com mais de um tipo de paradigma, como orientado a objetos, funcional, lógica, entre outros.

Quando em uma linguagem não precisamos declarar variáveis para usá-las dizemos que ela é tipicamente dinâmica.

Python é uma linguagem interpretada.



2a
          Questão	Acerto: 1,0  / 1,0
Considere o seguinte código em Python: 

a = 1

b = 2

c = a+b

print ("o resultado",c);

Suponha que este código esteja no arquivo teste.py, qual seria a chamada correta através do prompt do sistema operacional?

	
python teste

 Certo	
python teste.py

	
py teste.py

	
p teste

	
p teste.py

Respondido em 21/03/2023 02:25:51


Explicação:
A resposta é a letra d, pois um programa em python é chamado usando o comando python e o nome do arquivo com a terminação .py.

As outras chamadas não são funcionais.



3a
          Questão	Acerto: 1,0  / 1,0
Considere o código a seguir:

x = 10

soma = 0

while (x > 0):

               x = x - 2

               soma = soma + x

print(soma)

Após sua execução, o resultado será:

	
18

	
30

 Certo	
20

	
45

	
55

Respondido em 21/03/2023 02:26:25


Explicação:
Teste de mesa

A estrutra de repetição irá ocorrer enquanto x for maior que  0. Sendo assim, será executados os seguintes valores para x.

x: 8  soma: 8

x: 6  soma: 14

x: 4  soma: 18

x: 2  soma: 20

x: 0  soma: 20



4a
          Questão	Acerto: 1,0  / 1,0
Durante o desenvolvimento do projeto, foi necessário criar um método construtor para a classe Empregado. Assinale a opção que apresenta a criação do método construtor.

	
_init_(self, matricula, cargo):

	
def _empregado_(self, matricula, nome, cargo):

	
def _construtor_(self, matricula, nome, cargo):

 Certo	
def _init_(self, matricula, nome, cargo):

	
_empregado_(self, matricula, cargo):

Respondido em 21/03/2023 02:26:46


Explicação:
 O método construtor é criado através da sintaxe:

               def _init_():



5a
          Questão	Acerto: 1,0  / 1,0
Considere a seguinte definição da classe fração:

class Fracao:

    def __init__(self,num,den):

        self.num = num

        self.den = den

Qual seria um possivel cabeçalho para um método de multiplicar duas frações?

	
fracao.multiplicar(f1)

 Certo	
def __mul__(self,fracao):

	
Nenhuma das anteriores está correta.

	
f.multiplicar(f)

	
def mul(fracao1, fracao2) 

Respondido em 21/03/2023 02:27:08


Explicação:
A resposta é:

def __mul__(self,fracao):

onde é passado como parâmetro um objeto da classe Fracao de onde serão retirados o numerador e o denominador.

Abaixo o código desse método:

def mul(self,fracao):

        return Fracao(self.num*fracao.num,

                       self.den*fracao.den)



6a
          Questão	Acerto: 1,0  / 1,0
Qual o resultado dos seguintes comandos em Python?

lista1 = [1,2,3]

lista2 = [4,5,6]

print(lista1 + lista2)

 Certo	
[1,2,3,4,5,6]

	
[6,5,4,3,2,1]

	
[1,2,3]

	
[4,5,6]

	
[2,4,5,6]

Respondido em 21/03/2023 02:27:57


Explicação:
Comentário: a resposta é [1,2,3,4,5,6]. O operador + junta os elementos de duas listas.



7a
          Questão	Acerto: 0,0  / 1,0
Analise o seguinte código em Python:

estrutura = (3,4,6,4,5,'b','f',5,8,2)

print(estrutura.count(5))

Qual o nome dessa estrutura e o que será impresso no console?

	
array, 0

 Certo	
tupla, 2 

 Errado	
lista, 4 

	
fila, 2

	
dicionário, 2

Respondido em 21/03/2023 02:28:29


Explicação:
Essa estrutura se chama tupla e a função count(5) contará o número de vezes  que o elemento 5 aparece na estrutura, no caso duas vezes, a resposta é a tupla, 2.



8a
          Questão	Acerto: 1,0  / 1,0
Em Python, existem várias possibilidades de manipularmos textos e strings. Considere o seguinte código

line = 'teste,de,alguma,coisa'

print(line.split(','))

Qual será o resultado desse trecho? 

	
['testede','algumacoisa']

	
['teste', 'coisa']

	
testedealgumacoisa

	
[t,e,s,t,e]

 Certo	
['teste', 'de', 'alguma', 'coisa']

Respondido em 21/03/2023 02:28:58


Explicação:
A resposta certa é ['teste', 'de', 'alguma', 'coisa']. A função ¿split¿ divide a string de acordo com um parâmetro de entrada, nesse caso é a vírgula.



9a
          Questão	Acerto: 1,0  / 1,0
Para utilizarmos em Python funções matemáticas como por exemplo math.sqrt(2) precisamos em primeiro lugar carregar um módulo. Qual das instruções abaixo realiza essa situação?

	
load math package 

 Certo	
import math 

	
import all math functions 

	
Math.math

	
Math.load math

Respondido em 21/03/2023 02:29:13


Explicação:
Em Python utilizamos o comando ¿import¿ para carregar um módulo, no caso acima a intrução para carregar o módulo math seria ¿import math¿.



10a
          Questão	Acerto: 1,0  / 1,0
Considere o seguinte código:

from statistics import mean

Para calcularmos a média como fica a chamada da função?

	
statistics.mean([2,3,4])

	
math.statistics.mean([2,3,4])

	
math(2,3,4).final 

 Certo	
mean[2,3,4]

	
math(2,3,4) 

'''