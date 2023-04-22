pilha = []

pilha.insert(0,10)

pilha.insert(0,5)

pilha.insert(0,3)

pilha.insert(0,40)

pilha.pop(0)

pilha.insert(0,11)

pilha.insert(0,4)

pilha.insert(0,7)

pilha.pop(0)

pilha.pop(0)

print("Pilha.: ", sum(pilha))


'''
As estruturas de dados são formas de construir e armazenar informações para posterior recuperação. Dentre as estruturas podemos trabalhar com a Pilha.

Analisando o código abaixo, assinale a alternativa que equivale ao comando print("Pilha: ", pilha) ao final da execução do código. Sabe-se que a função insert permite inserir um elemento na pilha e a função pop permite retirar o elemento da pilha.

pilha = []

pilha.insert(0,10)

pilha.insert(0,50)

pilha.insert(0,40)

pilha.insert(0,120)

pilha.pop(0)

pilha.insert(0,15)

pilha.pop(0)

pilha.pop(0)

print("Pilha: ", pilha)

	
Pilha: [10, 50, 40, 120, 15]

	
Pilha: [15, 120, 40, 50, 10]

Certo		
Pilha: [ 50, 10]

	
Pilha: [120, 15]

	
Pilha: [40, 50]




Explicação:
Conceito de Pilha ¿ O último a entrar é o primeiro a sair.

Passo a passo da execução do código

Pilha.:  []   Pilha.:  [10]    Pilha.:  [50, 10]  Pilha.:  [40, 50, 10]     Pilha.:  [120, 40, 50, 10]       Pilha.:  [40, 50, 10]      Pilha.:  [15, 40, 50, 10]     Pilha.:  [40, 50, 10]   Pilha.:  [50, 10]




 	

2.
A pilha é uma estrutura de dados que permite a inserção/remoção de itens dinamicamente seguindo a norma de último a entrar, primeiro a sair. Suponha que para uma estrutura de dados, tipo pilha, são definidos os comandos insert (insere um elemento da pilha) e pop (remove um elemento da pilha.

Considere que, em uma estrutura de dados tipo pilha "pilha", inicialmente vazia, sejam executados os seguintes comandos:

 

pilha = []

pilha.insert(0,10)

pilha.insert(0,5)

pilha.insert(0,3)

pilha.insert(0,40)

pilha.pop(0)

pilha.insert(0,11)

pilha.insert(0,4)

pilha.insert(0,7)

pilha.pop(0)

pilha.pop(0)

print("Pilha.: ", pilha)

 

Após a execução dos comandos, o elemento no topo da pilha e a soma dos elementos armazenados na pilha são, respectivamente,

	
11 e 80

	
7 e 40

	
7 e 29

Certo		
11 e 29

	
4 e 80




Explicação:
Conceito de Pilha ¿ O último a entrar é o primeiro a sair.

Resultado final da Pilha.:  [11, 3, 5, 10]

Elemento que está no topo da pilha é o 11.

Soma dos elementos da pilha:  11+3+5+10 =29




 	

3.
Ao executarmos os seguintes comandos em Python qual o resultado que teremos?

lista = [4,2,1,5,0]

lista.sort()

print(lista)

	
[1,2,3,4,5]

	
[5,4,3,2,1]

	
[5,3,4,2,1]

Certo		
[0,1,2,4,5]

	
[5,4,2,1,0]




Explicação:
a resposta é [0,1,2,4,5], pois a função sort() ordena a lista do menor para o maior.




 	

4.
Listas são um dos principais tipos de dados em Python. Analise as afirmações a seguir.

Em Python, listas de objetos são representadas pelo tipo list. Esse tipo de dados é basicamente uma sequência de elementos, que podem ou não ser do mesmo tipo.
Python permite também a criação de listas aninhadas (uma lista dentro da outra). Este recurso é útil quando desejamos criar listas de várias dimensões (ou matrizes).
Em Python, normalmente percorremos listas de elementos sem que existam índices associados a eles.
 

Após a sua análise, assinale a opção em que são apresentadas apenas as afirmações corretas.

	
Somente a afirmativa: I.

Certo		
Estão corretas as afirmações: I, II e III.

	
Estão corretas as afirmações: II e III.

	
Estão corretas as afirmações: I e III.

	
Estão corretas as afirmações: I e II.




Explicação:
Vale destacar que o Python nos permite percorremos uma lista por meio de intervalos, usando a função range()




 	

5.
As estruturas de dados são formas de construir e armazenar informações para posterior recuperação. Dentre as estruturas podemos trabalhar com a Fila.

Analisando o código abaixo, assinale a alternativa que equivale ao comando print("Fila: ", fila) ao final da execução do código. Sabe-se que a função append permite inserir um elemento na fila e a função pop permite retirar o elemento da fila.

fila = []

fila.append(10)

fila.append(3)

fila.append(5)

fila.append(8)

fila.pop(0)

fila.pop(0)

fila.append(20)

print("Fila: ", fila)

	
Fila: [5, 8]

	
Fila: [10, 3, 5, 8, 20]

Certo		
Fila: [ 5, 8, 20]

	
Fila: [20, 8, 5]

	
Fila: [10, 3, 5, 8]




Explicação:
Conceito de Fila ¿ O primeiro a entrar é o primeiro a sair.

Passo a passo da execução do código

Fila:  []    Fila:  [10]    Fila:  [10, 3]   Fila:  [10, 3, 5]       Fila:  [10, 3, 5, 8]   Fila:  [3, 5, 8]   Fila:  [5, 8]  Fila:  [5, 8, 20]




 	

6.
Existem várias políticas de enfileiramento para o tipo abstrato de dados ¿Fila¿. Desses, qual é a sigla que define uma fila onde o primeiro a entrar é o primeiro a sair da fila?

	
pilha enfileirada

	
fila enfileirada

	
fila encadeada

Certo		
FIFO 

	
fila por prioridade




Explicação:
O termo FIFO significa ¿First in, First out¿ que significa que o primeiro a entrar é o primeiro a sair, então a resposta certa é FIFO.




 	

7.
Qual o resultado dos seguintes comandos em Python?

lista1 = [1,2,3]

lista2 = [4,5,6]

print(lista1 + lista2)

	
[6,5,4,3,2,1]

Certo		
[1,2,3,4,5,6]

	
[2,4,5,6]

	
[1,2,3]

	
[4,5,6]
'''

