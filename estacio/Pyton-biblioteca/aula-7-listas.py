lista_num=[10,50,90,30,50,90,70]
print(min(lista_num))#← valor mínimo 10
print(max(lista_num))#← valor máximo 90
print(sum(lista_num)) # somatorio de todos os valores


# inserção de elementos

estados = ['SP','RJ','ES'] #← lista de estados da região sudeste
print(estados)#['SP', 'RJ', 'ES'] #← mostramos os estados inseridos
estados.append('MG') #← inserindo ‘MG’ no final da lista
print(estados)# ['SP', 'RJ', 'ES', 'MG']


#REMOÇÃO DE ELEMENTOS

print(estados)#['SP', 'RJ', 'ES', 'MG'] ← lista original
#estados.pop(4) #← tentando remover da posição 4 ← erro, a posição não existe
estados.pop(0) #← removendo da posição 0
print(estados) # ← veja como ficou a lista
estados.pop()#← executar pop() sem parâmetro remo- veja o último elemento

# CLASSIFICAÇÃO (ORDENAÇÃO) DOS ELEMENTOS
estados.append('MG') 
estados.sort()

import random #← importação da biblioteca random
random.shuffle(estados) #← uso do shuffle() para embaralhar a lista
print(estados)
estados.reverse() #← classificação decrecente
print(estados)

#INSERÇÃO DE ELEMENTOS EM POSIÇÃO ESPECÍFICA
estados.insert(1,'SP')   
print(estados)

#CONTAGEM DE OCORRÊNCIAS DO ELEMENTO
estados.append('MG')
estados.append('MG')
print(estados)
print(estados.count('MG'))
print(estados)
print(estados.count('RJ'))

#RETORNO DO ÍNDICE DA PRIMEIRA OCORRÊNCIA DO ELEMENTO
print(estados)
print(estados.index('MG'))


#PROLONGAÇÃO(extensão)
sul = ['PR','SC','RS'] #← criamos a lista do sul
estados = ['ES','MG','RJ','SP'] #← lista de estados original
estados.extend(sul) #← prolongando a lista de estados
print(estados) #ES', 'MG', 'RJ', 'SP', 'PR', 'SC', 'RS']             ← nova lista de estados

#Estruura de dados 


##Fila
'''
Em uma empresa, sempre existe impressora de rede compartilhada para que os funcionários possam usá-la.
Os trabalhos são inseridos em uma fila para organizar a ordem das impressões. 
Aqueles enviados logo são atendidos primeiro, e assim por diante.

Aplicações 
Fila de impressão;
FIFO na logística para estocagem de materiais;
FIFO na contabilidade para avaliação do ativo circulante, a fim de apurar o total do lucro de uma empresa em determinado período de tempo.
'''
fila = []


#Pilha
'''
Nos sistemas operacionais, existe a pilha de execução, em que as instruções e os dados vão sendo empilhados e,
após execução, desempilhados, de acordo com a ordem de chegada.

Heap e stack no sistema operacional;
Vagões de trem – não é possível retirar um vagão do meio do trem;
Buffer para gravação de dados em memória;
LIFO ou UEPS na logística para estocagem de materiais;
LIFO na contabilidade para avaliação do ativo circulante, a fim de apurar o total do lucro de uma empresa em determinado período de tempo.
'''

pilha = []
pilha.insert(0, 1)
pilha.insert(0, 2)
pilha.insert(0, 3)
pilha.insert(0, 4)
pilha.insert(0, 5)
print(pilha) 

pilha.pop(0)
print(pilha) 
pilha.pop(0)
print(pilha) 
pilha.pop(0)
print(pilha) 

