#FIFO (First In, First Out) = O primeiro a entrar é o primeiro a sair.
class Fila:
    def __init__(self):
        self.dados = []
        

    def enqueue(self, elemento):#aqui vai a implementação do enqueue
        self.dados.append(elemento)   

    def dequeue(self):#aqui vai a implementação do dequeue
        if len(self.dados) < 1:
            return None
        return self.dados.pop(0)

    def vazia(self):
         return len(self.dados) == 0
     
    def exibir(self):
        if self.vazia == False:
            raise Exception("Lista esta vazia")
        print(self.dados)

fila = Fila() 
fila.exibir()
i =0
while i<10:
    fila.enqueue(i)
    i+= 1

fila.exibir()
fila.dequeue()
fila.exibir()
fila.dequeue()
fila.exibir()
fila.dequeue()




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
