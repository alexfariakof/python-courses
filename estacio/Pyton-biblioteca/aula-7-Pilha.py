class Pilha(object):
    def __init__(self):
        self.dados = []

    def push(self, elemento):
        self.dados.insert(0, elemento)

    def pop(self):
        self.dados.pop(0)
        
    def mostar(self):
        print(self.dados)


pilha = Pilha()
pilha.push(3)
pilha.push(5)
pilha.push(9)
pilha.push(10)
pilha.push(20)
pilha.mostar()
pilha.pop()
pilha.mostar()
pilha.pop()
pilha.mostar()
pilha.pop()

#Pilha LIFO
'''
Nos sistemas operacionais, existe a pilha de execução, em que as instruções e os dados vão sendo empilhados e,
após execução, desempilhados, de acordo com a ordem de chegada.

Heap e stack no sistema operacional;
Vagões de trem – não é possível retirar um vagão do meio do trem;
Buffer para gravação de dados em memória;
LIFO ou UEPS na logística para estocagem de materiais;
LIFO na contabilidade para avaliação do ativo circulante, a fim de apurar o total do lucro de uma empresa em determinado período de tempo.
'''
