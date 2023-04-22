'''
Considere o seguinte código:

from statistics import mean

Para calcularmos a média como fica a chamada da função?

	
statistics.mean([2,3,4])

Certo		
mean[2,3,4]

	
math(2,3,4) 

	
math.statistics.mean([2,3,4])

	
math(2,3,4).final 




Explicação:
Quando usamos o comando import em python não precisamos utilizar o nome do pacote antes do comando, no caso para calcular a média precisamos chamar apenas mean([2,3,4]), logo a resposta correta é mean[2,3,4]




 	

2.
Qual seria uma possível chamada para utilizar um módulo de um determinado pacote em Python?

	
export pacote

	
import pacote

Certo		
import pacote.modulo

	
import modulo.pacote

	
import modulo




Explicação:
a sintaxe correta é import pacote.modulo. Em Python temos sempre o pacote (que é uma coleção de módulos) e o módulo correspondente. 




 	

3.
Considere um arquivo que contenha as funções soma, subtração, multiplicação e divisão. Esse arquivo poderia ser um módulo: 

Certo		
de funções matemáticas 

	
de funções de rede

	
de funções relacionadas somente a inteiros

	
de funções relacionadas a strings 

	
de funções de computação gráfica 




Explicação:
Um módulo em Python é um arquivo contendo definições de funções e instruções. No caso da questão, como as funções se referem a matemática, a resposta correta seria "de funções matemáticas".




 	

4.
Avalie as assertivas a seguir, no que se refere aos conceitos de módulos e pacotes.

I. Tanto módulo como pacote são formas de organizarmos os arquivos que compõem o projeto do software.

II. Mas há diferença entre os 2 conceitos

III. Os módulos são organizados em pastas e os pacotes organizados em arquivos

Assinale a UNICA opção que apresente APENAS TODAS as assertivas corretas.

	
I, II e III

Certo		
Apenas I e II

	
Apenas I e III

	
Apenas I

	
Apenas II e III




Explicação:
I. Tanto módulo como pacote são formas de organizarmos os arquivos que compõem o projeto do software. - verdade

II. Mas há diferença entre os 2 conceitos  - verdade

III. Os módulos são organizados em pastas e os pacotes organizados em arquivos - FALSO ao contrário - modulos são organizados em arquivos e pacotes organizados em pastas




 	

5.
Vamos supor o seguint trecho de código em Phyton, dentro do módulo frete.py

 >>>import transportes.logistica.frete
 >>>transportes.logistica.frete.entrega()

O que faz o segundo comando acima ( >>>transportes.logistica.frete.entrega() ) ?

 


                                               

	
Importaçao do módulo

	
Importação da função de nome entrega

Certo		
uso da função de nome entrega

	
Leitura do módulo frete.py

	
O comando está incorreto e não executa




 	

6.
Como a linguagem PHYTON identifica que trata-se de um pacote ?

	
Por um arquivo especial, chamado _This_a_package

	
Não existe uma forma objetiva de saber

	
Pela existencia de um arquivo, na raiz principal da pasta, de nome _This_is_a_Package.

	
Pelo cabeçalho no pacote, contendo a identificação _PY_package

Certo		
Pela existencia, na estrutura de pastas, do arquivo _init_.py


'''