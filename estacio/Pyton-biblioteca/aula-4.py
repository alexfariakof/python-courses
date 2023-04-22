i = 0
while (i < 3):
    print ('Contagem:', i)
    i = i + 1
print ("Acabou!")


var = 1
while (var <= 3):
    num =  int(input("Digite um número:"))
    print ("Você digitou: ", num)
    var+=1
print ("Acabou!")

i = 0
while (i < 5):
    print (i, " é menor do que 5")
    i = i + 1
else:
    print (i, " não é menor do que 5")
    
for i in range (1, 11):
    print (i, 'Contagem: ', i)
print ('Agora acabou.')

'''
Tipo	Descrição
if	Usado para executar uma ação, caso uma condição seja verdadeira.
Else	Usado quando a condição não for satisfeita.
Elif	Usado se mais de uma condição alternativa.
'''


var1 = 100
if var1:
    print ("1 – Valor verdadeiro")
    print (var1)
else:
    print ("1 – Valor falso")
    print (var1)
var2 = 0
if var2:
    print ("2 – Valor verdadeiro")
    print (var2)
else:
    print ("2 – Valor falso")
    print (var2)
print ("Adeus!")

# Operadoresd de comparação
'''
Símbolo	Definição
==	Igual
!=	Diferente
>	Maior que
<	Menor que
>=	Maior ou igual
<=
Menor ou igual
'''

idade = int (input ('Digite sua idade: '))
if idade >= 10 and idade < 20:
    print ('Você é adolescente')
elif idade >= 20 and idade < 30:
    print ('Você é jovem')
elif idade >= 30 and idade <= 100:
    print ('Você é adulto')
else:
    print ('Valor não encontrado!')
    
# IMC = peso/(altura*altura)
'''
Valor do IMC	Classificação
Abaixo de 17	Muito abaixo do peso
Entre 17 e 18,49	Abaixo do peso
Entre 18,5 e 24,99	Peso normal
Entre 25 e 29,99	Acima do peso
Entre 30 e 34,99	Obesidade I
Entre 35 e 39,99	Obesidade II (severa)
Acima de 40	Obesidade III (mórbida)
'''

peso = input ('Digite o seu peso em Kg:')
altura = input ('Digite sua altura em m: ')
imc = float(peso)/(float(altura)*float (altura))
if imc <= 17:
    print ("Muito abaixo do peso")
elif imc > 17 and imc < 18.5:
    print ("Abaixo do peso")
elif imc > 18.5 and imc < 25:
    print ("Peso normal")
elif imc > 25 and imc < 30:
    print ("Acima do peso")
elif imc > 30 and imc < 25:
    print ("Obesidade I")
elif imc > 35 and imc < 40:
    print ("Obesidade II(severa)")
else:
    print ("Obesidade III(mórbida)")
