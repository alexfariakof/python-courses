#tuplas, há um detalhe importante: elas são imutáveis.
#E existem aplicações para isso.
tupla = ('t', 'u', 'p', 'l', 'a')
print(tupla[2:])
print(tupla[3:])
print(tupla[:])
print(tupla[2:]+(tupla[3:]))
for i in tupla:
    print(i)

#VERIFICAR QUANTOS ELEMENTOS EXISTEM NA TUPLA
len(("Olá","mundo","do","Python"))

#CONCATENAR TUPLAS

parte1=("Ouviram","do","Ipiranga")
parte2=("as","margens","plácidas")
verso1 = parte1+parte2 #verso1('Ouviram', 'do', 'Ipiranga', 'as', 'margens', 'plácidas')

#REPETIR ELEMENTOS
#Para isto, usamos o operador “*”:
mi=('mi',) # ← Note o detalhe da vírgula!
mi*10 #('mi', 'mi', 'mi', 'mi', 'mi', 'mi', 'mi', 'mi', 'mi', 'mi')

# VERIFICAR SE UM ELEMENTO PERTENCE À TUPLA

print('O elemento U existe na tupla %s' % ('u' in tupla)) #True
'f' in tupla #false

# ITERAR NOS ELEMENTOS
seila = {}
seila[1] = 1
seila['1'] = 2
seila[1] += 1

soma = 0
for k in seila:
        soma += seila [k]
print(soma)
