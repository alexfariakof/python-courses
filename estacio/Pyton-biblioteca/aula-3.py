out = 'primeira linah texto 1 \.'
print(out)

''' Conversores de Tipo
int(x [,base])	Converte x para um número inteiro. Nesse caso, podemos usar uma base para o número.
float(x)	Converte x para um número de ponto flutuante.
str(x)	Converte x para string.
repr(x)	Converte x para uma string de expressão.
set(s)	Converte s para um conjunto.
chr(x)	Converte um inteiro para um caractere.
unichr(x)	Converte um inteiro para um caractere Unicode.
ord(x)	Converte um único caractere para seu valor inteiro.
hex(x)	Converte um inteiro para uma string hexadecimal.
oct(x)	Converte um inteiro para uma string octal.
'''

''' Funções String 
>>> testando = "Olá Mundo!"
2	>>> print(testando)              #Saída: Olá Mundo!
3	>>> print(testando[0])           #Saída: O
4	>>> print(testando[4])           #Saída: M
5	>>> print(testando[2:6])         #Saída: á Mu
6	>>> print(testando[3:])          #Saída: Mundo!
7	>>> print(testando*2)            #Saída: Olá Mundo!Olá Mundo!
'''

# Calculando IMC 
altura = input('Digite sua altura em metros: ')
peso = input('Digite o seu peso em KG:') 
imc = float(peso)/(float(altura)*float(altura))
print(imc)

numero  =input('Digite um número: ')
print('O número informando é ' + numero)


nota1 = input('Entre com a primeira nota: ')
nota2 = input('Entre com a segunda nota: ')
nota3 = input('Entre com a terceira nota: ')
nota4 = input('Entre com a quarta nota: ')
media = (float(nota1)+float(nota2)+float(nota3)+float(nota4))/4
print(media)