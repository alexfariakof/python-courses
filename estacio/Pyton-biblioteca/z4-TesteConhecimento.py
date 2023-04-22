Para acessar o atributo de um objeto Python, pode ser utilizado, alternativamente ao acesso direto, a seguinte função:

	
delattr

	
setattr

	
hasattr

	
expattr

Certo		
getattr




Explicação:
Funções: getattr - retorna o valor do atributo, hasattr - testa se existe o atributo, setattr - seta o valor do atributo, delattr - remove o atributo, expattr - não existe.




 	

2.
Durante o desenvolvimento do projeto, foi necessário criar um método construtor para a classe Empregado. Assinale a opção que apresenta a criação do método construtor.

	
def _construtor_(self, matricula, nome, cargo):

Certo		
def _init_(self, matricula, nome, cargo):

	
_init_(self, matricula, cargo):

	
_empregado_(self, matricula, cargo):

	
def _empregado_(self, matricula, nome, cargo):




Explicação:
 O método construtor é criado através da sintaxe:

               def _init_():




 	

3.
Toda linguagem orientada a objetos permite a especificação de métodos construtores na classe, os quais são responsáveis pela inicialização do objeto recém-alocado na memória. Na linguagem Python este método recebe o seguinte nome:

	
self

Certo		
__init__

	
def

	
constructor

	
this




Explicação:
O método construtor é denominado __init__, sendo definido, como os demais métodos, através de def __init__(self, parâmetros...). Quanto aos demais, def serve para criar uma função ou método e self é o ponteiro de auto-referência implícito do Python. O this e o constructor não pertencem à sintaxe Python.




 	

4.
Durante o desenvolvimento de um programa em Pyhton foi criada a função cadastro, a qual recebe como parâmetros o nome e a idade de uma pessoa, respectivamente.

Assinale a alternativa que executa a função corretamente.

Certo		
cadastro("Paulo", 20)

	
cadastro (20, "Paulo")

	
def cadastro(20, "Paulo")

	
def cadastro ("Paulo", 20)

	
cadastro()




Explicação:
Para chamarmos uma função devemos usar a seguinte sintaxe:

                         Nome da função (parâmetros de entrada)




 	

5.
Assinale a alternativa que implementa a função IMC. Esta função recebe como parâmetro de entrada  o peso e a altura de uma pessoa e retorna com o valor do IMC.

	
IMC(peso, altura):

                calculo = float(peso) / float(altura) * float (altura))

               print(calculo)

	
IMC(peso, altura):

                calculo = float(peso) / float(altura) * float (altura))

               return calculo

Certo		
def IMC(peso, altura):

                calculo = float(peso) / float(altura) * float (altura))

               return calculo

	
IMC():

                calculo = float(peso) / float(altura) * float (altura))

               return calculo

	
def IMC(peso, altura):

                calculo = float(peso) / float(altura) * float (altura))

               print(calculo)




Explicação:
Estrutura de uma função em Pyhton:

Toda função em Python começa com o comando def.
Depois do def, há o nome da função.
Em seguida, aparece a lista de parâmetros, que pode estar vazia, mas os parênteses são obrigatórios.
Após essa lista, estão os dois pontos (¿:¿).
Todo o código que estiver indentado fará parte do corpo da função. A indentação é muito importante na definição de funções.
Toda função termina com o comando return, que pode ser seguido ou não de uma variável de retorno.



 	

6.
Em orientação a objetos, a característica que determina a possibilidade de um descendente alterar a funcionalidade de um método herdado é deominada:

	
herança

	
encapsulamento

	
composição

Certo		
polimorfismo

	
abstração




Explicação:
Através da herança é possível criar uma nova classe a partir de outra já existente, aproveitando suas características, mas algumas funcionalidades podem não ser adequadas, podendo ser modificadas através da sobrescrita destes métodos, segundo um processo denominado polimorfismo.




 	

7.
 Ao definirmos uma classe Carro em Python, qual seria um possível método para ela? 

	
def somar(a,b):

	
define plantar(lugar):

	
define acender(valor):

	
define fechar():

Certo		
def acelerar(vel):




Explicação:
A resposta é a letra b, porque um método é uma ação a ser executado pelo objeto, no caso, um carro possui como uma ação possível a aceleração, as letras c, d e e estão com uma palavra chave define que não é do python, e a letra a, somar dois parâmetros não se encaixa no objeto carro.

