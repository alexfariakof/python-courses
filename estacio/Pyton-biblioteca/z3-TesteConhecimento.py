#Atenção ao gabarito da questão 1 onde a senteça correta é i<45 :
# a Resposta correta da questão é i<=45 que gerar 46 resultados está incorreta 
x = 10

soma = 0

while (x > 0):
    x = x - 2
    soma = soma + x
print(soma)



soma = 0

while i<45:
    i = i + 1
    print(i)
    
    
preco = 121    
if preco > 120:
    desconto = preco * 0.15
print(preco-desconto)
print(preco * 0.85)


valor = 7

while (valor>3):
    print(valor)
    valor -= 1
else:
    ultimo_valor = valor
    print(ultimo_valor)
i = 1

'''


Uma empresa deseja saber qual será o valor total da folha de pagamento de seus funcionários no próximo mês.

Analise o programa abaixo (em Python) .

i = 1

soma = 0

while __________________ # sentença 1

sal = float( input('Salário..: ') )

               soma = soma + sal

               i = i + 1

print("Total da Folha de Pagamento..: R$ ", soma)

 

Sabe-se que a empresa possui 45 funcionários. Complete a sentença 1 de forma que o programa ao final apresente o Valor Total da Folha de pagamento da empresa.

	
( i >= 45):

Certo		
( i <= 45):

	
( i < 45 ):

	
( i > 45 ):

	
( i = 45 ):




Explicação:
Enquanto a condição for verdadeira a estrutura de repetição é executada. Sendo assim, como a empresa possui 45 funcionários e i começa com 1, a condição é i<=45.




 	

2.
Analise as informações abaixo:

Python é interpretado
Python é orientado a objetos
Python é interativo
Estão corretas as afirmações:

	Somente I e II
	Somente II e III
Certo		I, II e III
	Somente I e III
	Somente I



Explicação: Todas as afirmações estão corretas



 	

3.
Uma empresa deseja conceder um desconto de 15% para as vendas acima de R$ 120,00. Assinale o trecho de programa que implementa de forma correta a estrutura condicional, onde a variável preco conterá o valor a ser pago, já incluindo o desconto.

	
if preco > 120:

               preco = preco * 0.15

	
if preco > 120:

               preco = preco * 1.15

	
if preco >= 120:

               preco = preco * 1.15

	
if preco >= 120:

               preco = preco * 0.15

Certo		
if preco > 120:

               preco = preco * 0.85




Explicação:
Para calcularmos o desconto trabalhamos coma seguinte fórumla:

Valor do desconto:  preco * Percentual do desconto / 100

Valor com desconto: preco - preco * Percentual do desconto / 100 ou preco *0.85

A questão pede o preço com o desconto.




 	

4.
 Qual é a função do operador relacional ¿==¿ em Python?

	
atribuição

	
diferente

	
ou lógico 

	
e lógico 

Certo		
igual




Explicação:
== signfica o operador lógico de igualdade em Python, neste caso a resposta é a letra a. 




 	

5.
Uma loja de varejo, deseja classificar seus produtos em  Promo10, Promo20 e Promo30, de acordo com a tabela abaixo.

          Preço do Produto (preco)           

     Classificação    

<= R$ 10,00

Promo10

Entre R$ 10,00 e R$ 50,00

Promo20

>= R$ 50,00

Promo30

Assinale o trecho de programa que implementa de forma correta a estrutura condicional.

	
if preco <= 10.00:

                print("Promo 10")

elif preco > 50.00 :

               print("Promo 20")

else:

              print("Promo 30")

	
if preco <= 10.00:

                print("Promo 10")

elseif preco < 50.00 :

               print("Promo 20")

else:

              print("Promo 30")

Certo		
if preco <= 10.00:

                print("Promo 10")

elif preco < 50.00 :

               print("Promo 20")

else:

              print("Promo 30")

	
if preco <= 10.00:

                print("Promo 10")

elif preco >10.00 or preco < 50.00 :

               print("Promo 20")

else:

              print("Promo 30")

	
if preco <= 10.00:

               print("Promo 10")

                elif preco < 50.00 :

                               print("Promo 20")

else:

                                              print("Promo 30")




Explicação:
As estruturas de decisão em Python são:

Tipo	Descrição
if	Usado para executar uma ação, caso uma condição seja verdadeira.
Else	Usado quando a condição não for satisfeita.
Elif	Usado se mais de uma condição alternativa.
 

Em Python, o comando if possui a seguinte sintaxe:


if expressão:
       comando(s)
else:
       comando(s)

 

É obrigatória a identação para criar o bloco de comandos.




 	

6.
Considere o seguinte código em Python:

valor = 7

while (valor>3):

  print(valor)

  valor -= 1

else:

  ultimo_valor = valor

  print(ultimo_valor)

Qual é o resultado da variável ¿ultimo_valor¿, quando terminar o código?

	
7

	
6

Certo		
3

	
4

	
5




Explicação:
A condição é imprimir enquanto o valor for maior que 3. Quando chegar ao valor 3,  o código executará a instrução else, e terá o valor igual a 3.

A resposta correta é a letra e.




 	

7.
Considere o código a seguir:

x = 10

soma = 0

while (x > 0):

               x = x - 2

               soma = soma + x

print(soma)

Após sua execução, o resultado será:

	
45

	
30

	
55

	
18

Certo		
20




Explicação:
Teste de mesa

A estrutra de repetição irá ocorrer enquanto x for maior que  0. Sendo assim, será executados os seguintes valores para x.

x: 8  soma: 8

x: 6  soma: 14

x: 4  soma: 18

x: 2  soma: 20

x: 0  soma: 20
'''




