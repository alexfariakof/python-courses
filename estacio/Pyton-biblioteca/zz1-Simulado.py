'''
lista1 = [1,2,3]
lista2 = [4,5,6]
print(lista1 + lista2)
'''

my_dict = {"a": 1, "b": 2}
valor = my_dict["a"]
valor = my_dict.get("a")
print(valor)


line = 'teste,de,alguma,coisa'
print(line.split(','))

'''
Questão	Acerto: 1,0  / 1,0
O que será impresso pelo código seguinte?

print("ABC")#DEF

#print("GHI")

print("#JK")#LM

print("NO#PQ")

	
ABCDEFGHIJKLMNOPQ

	
ABCNO

	
ABCJKNOPQ

	
ABC#DEF#JK#LMNO#PQ

 Certo	
ABC#JKNO#PQ

Respondido em 20/03/2023 22:14:14


Explicação:
Os únicos elementos que constituem comentários são: #DEF, #print("GHI"), #LM. Todos os demais serão impressos na ordem em que ocorrem no código.



2a
          Questão	Acerto: 1,0  / 1,0
Seja a string em Python:

str = 'Python';

Qual o resultado da expressão:

print(str[0]);

	
h

	
y

	
t

	
o

 Certo	
P

Respondido em 20/03/2023 22:14:30


Explicação:
A resposta é P, pois em python as cadeias de caracteres começam com o primeiro elemento 0 (zero).



3a
          Questão	Acerto: 1,0  / 1,0
Considere o seguinte código em Python:

valor = 7

while (valor>3):

  print(valor)

  valor -= 1

else:

  ultimo_valor = valor

  print(ultimo_valor)

Qual é o resultado da variável ¿ultimo_valor¿, quando terminar o código?

	
4

	
6

	
7

	
5

 Certo	
3

Respondido em 20/03/2023 22:16:02


Explicação:
A condição é imprimir enquanto o valor for maior que 3. Quando chegar ao valor 3,  o código executará a instrução else, e terá o valor igual a 3.

A resposta correta é a letra e.



4a
          Questão	Acerto: 1,0  / 1,0
Para acessar o atributo de um objeto Python, pode ser utilizado, alternativamente ao acesso direto, a seguinte função:

	
hasattr

	
delattr

	
expattr

 Certo	
getattr

	
setattr

Respondido em 20/03/2023 22:16:12


Explicação:
Funções: getattr - retorna o valor do atributo, hasattr - testa se existe o atributo, setattr - seta o valor do atributo, delattr - remove o atributo, expattr - não existe.



5a
          Questão	Acerto: 1,0  / 1,0
O que o código abaixo imprime?
class Vendas:
    def __init__(self, id):
        self.id = id
        id = 100

val = Vendas(123)
print (val.id)

	Nada. Vai dar pau
	Id
	Nenhuma das anteriores
 Certo	123
	100
Respondido em 20/03/2023 22:16:21


Explicação: O construtor vai fazer a atribuição para a variável id do objeto val


6a
          Questão	Acerto: 1,0  / 1,0
Qual o resultado dos seguintes comandos em Python?

lista1 = [1,2,3]

lista2 = [4,5,6]

print(lista1 + lista2)

	
[1,2,3]

	
[4,5,6]

	
[6,5,4,3,2,1]

	
[2,4,5,6]

 Certo	
[1,2,3,4,5,6]

Respondido em 20/03/2023 22:17:38


Explicação:
Comentário: a resposta é [1,2,3,4,5,6]. O operador + junta os elementos de duas listas.



7a
          Questão	Acerto: 1,0  / 1,0
Em Python, dicionário é um tipo de estrutura de dados em que há mapeamento entre uma chave (key) e um valor (value). Qual é o método utilizado para obter o conteúdo associado à chave?

	
key()

	
set()

	
value()

	
items()

 Certo	
get()

Respondido em 20/03/2023 22:28:54


Explicação:
Dicionários - Métodos:

value() - Permite visualizar os valores armazenados.

set() ¿ não existe este método.

key() - Permite identificar as chaves de um dicionário.

items() - Permite retornar os elementos na forma de tuplas.



8a
          Questão	Acerto: 1,0  / 1,0
Em Python, existem várias possibilidades de manipularmos textos e strings. Considere o seguinte código

line = 'teste,de,alguma,coisa'

print(line.split(','))

Qual será o resultado desse trecho? 

	
testedealgumacoisa

	
[t,e,s,t,e]

	
['testede','algumacoisa']

 Certo	
['teste', 'de', 'alguma', 'coisa']

	
['teste', 'coisa']

Respondido em 20/03/2023 22:29:45


Explicação:
A resposta certa é ['teste', 'de', 'alguma', 'coisa']. A função ¿split¿ divide a string de acordo com um parâmetro de entrada, nesse caso é a vírgula.



9a
          Questão	Acerto: 0,0  / 1,0
Avalie cada assertiva a seguir no que se refere a aplicação dos conceitos de escopo e tempo de vida de uma variável

I. Não é possível  ter uma variável local a uma função com mesmo nome de uma variável global

II. Uma variável local só é reconhecida enquanto a função estiver em execução

III. A forma de defirmos em Phyton que uma variável usada internamente em uma função é na verdade global, é inserir o termo global antes da referencia a variável, dentro da função. Algo  como  global ind, sendo "ind" o nome da variável global.

Assinale a Unica opção que apresenta a resposta com as assertvas corretas

	
Apenas I e II

	
I, II e III

 Certo	
Apenas II e III

 Errado	
Apenas II

	
Apenas III

Respondido em 20/03/2023 22:31:31


Explicação:
I. Não é possível  ter uma variável local a uma função com mesmo nome de uma variável global - FALSO, é possível sim

II. Uma variável local só é reconhecida enquanto a função estiver em execução --> VERDADE

III. A forma de defirmos em Phyton que uma variável usada internamente em uma função é na verdade global, é inserir o termo global antes da referencia a variável, dentro da função. Algo  como  global ind, sendo "ind" o nome da variável global. -->VERDADE



10a
          Questão	Acerto: 1,0  / 1,0
Como a linguagem PHYTON identifica que trata-se de um pacote ?

	
Por um arquivo especial, chamado _This_a_package

	
Pelo cabeçalho no pacote, contendo a identificação _PY_package

 Certo	
Pela existencia, na estrutura de pastas, do arquivo _init_.py

	
Não existe uma forma objetiva de saber

	
Pela existencia de um arquivo, na raiz principal da pasta, de nome _This_is_a_Package.
'''