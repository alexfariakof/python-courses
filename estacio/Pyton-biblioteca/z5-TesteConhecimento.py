Seja a classe definida como FormaGeométrica em Python, qual das opções abaixo poderia ser uma classe herdada dessa classe?

	
class Carro(FormaGeometrica)

	
class Pessoa(FormaGeometrica)

Certo		
class Quadrado(FormaGeometrica) 

	
Nenhuma das opções está correta.

	
class Animal(FormaGeometrica) 




Explicação:
A resposta é class Quadrado(FormaGeometrica), classe Quadrado, porque uma subclasse herda as propriedades da superclasse, e como só existe uma única forma geométrica entre as opções ela é a resposta correta. 




 	

2.
Qual é a saída do comando abaixo: >>> a='10' >>> print(a*2)
	`20¿
	Erro!
	20
	100
Certo		1010



Explicação: A variável a contém uma string. Usar o operador "*" vai repeti-la



 	

3.
Qual é o objetivo do comando super() na declaração abaixo?

class Carro(Veiculo):

  def __init__(self,vel,marca):

    super().__init__(vel)

    self.marca = marca

	
Nenhuma das respostas anteriores está correta.

	
Apenas a sintaxe normal para a definição de uma classe simples em Python.

Certo		
Permite que a classe herde o método da superclasse.

	
Inicializa a variável vel.

	
Uso de polimorfismo em Python.




Explicação:
A resposta é letra a. É desse modo que se implementa a sobrecarga de métodos em Python, possibilitando extender a funcionalidade da superclasse para as classes filhas.




 	

4.
O que o código abaixo imprime?
class Vendas:
    def __init__(self, id):
        self.id = id
        id = 100

val = Vendas(123)
print (val.id)

	Nenhuma das anteriores
	100
Certo		123
	Id
	Nada. Vai dar pau



Explicação: O construtor vai fazer a atribuição para a variável id do objeto val



 	

5.
Qual das opções abaixo contém conceitos apenas do paradigma orientado a objetos?

	
 função, variável

	
variável, estrutura condicional

	
atribuição, algoritmo

	
classe, estrutura de repetição

Certo		
método, classe, herança




Explicação:
A resposta é a letra a, que possui três conceitos que se aplicam a orientação a objetos.




 	

6.
Considere a seguinte definição da classe fração:

class Fracao:

    def __init__(self,num,den):

        self.num = num

        self.den = den

Qual seria um possivel cabeçalho para um método de multiplicar duas frações?

	
fracao.multiplicar(f1)

	
f.multiplicar(f)

Certo		
def __mul__(self,fracao):

	
Nenhuma das anteriores está correta.

	
def mul(fracao1, fracao2) 




Explicação:
A resposta é:

def __mul__(self,fracao):

onde é passado como parâmetro um objeto da classe Fracao de onde serão retirados o numerador e o denominador.

Abaixo o código desse método:

def mul(self,fracao):

        return Fracao(self.num*fracao.num,

                       self.den*fracao.den)




 	

7.
Qual dos comandos abaixo define uma relação de herança em Python?

	
class Carro extends Veiculo 

	
class Carro is Veiculo

Certo		
class Carro(Veiculo) :

	
class Carro inherits Veiculo

	
Carro is Veiculo 




Explicação:
A resposta é a letra a, que tem a sintaxe correta para definir, em Python, que a classe Carro é uma extensão da classe Veiculo.




 	

8.
A função abaixo em Python ilustra um conceito muito importante no paradigma funcional.

def fatorial(valor):

    if valor == 0:

        return 1

    else:

        return valor * fatorial(valor-1)

Qual é esse conceito?

	
Linguagens de script 

	
Orientação a objetos 

Certo		
Recursividade

	
Tipagem dinâmica

	
Multiparadigmas




Explicação:
A resposta é a letra c. A função implementa a função fatorial que chama a ela mesma no comando else. Esse conceito de uma função chamar ela mesma é definido por recursividade.