'''
Mecanismo mais relacionado com reuso de código dentro da orientação a objetos – uma grande vantagem desse tipo de paradigma.

Exemplo

Uma criança herda características de seus pais, estes herdam de seus avós, os avós dos bisavôs, e assim por diante. Na orientação a objetos, um objeto abaixo de uma hierarquia herda características de todos os objetos superiores a ele.


ABSTRAÇÃO
O problema de qualquer engenheiro de software é transportar para o mundo computacional uma visão da realidade de acordo com o paradigma que escolheu para desenvolver o projeto.

No caso da orientação a objetos, a abstração envolve três questões:

1. Todo objeto precisa ter uma identidade.
2. Todo objeto possui propriedades, ou seja, os elementos que o definem.
3. Todo objeto possui métodos ou ações que executa.

Portanto, podemos abstrair elementos do mundo real e convertê-los em objetos para que sejam implementados em alguma linguagem orientada a objetos.


ENCAPSULAMENTO
Pilar que esconder as propriedades de um objeto, tornando o programa mais seguro e deixando à mostra somente as ações que o objeto pode executar.

Basicamente, quando usamos propriedades privadas relacionadas a métodos assessores (get e set), evitamos o acesso direto à propriedade do objeto, aumentando a segurança da aplicação.

Exemplo

Quando assistimos à TV, só nos preocupamos com o ato de ligar ou desligar o aparelho, o que ocorre internamente. Mas os circuitos envolvidos dentro da televisão não são de nosso conhecimento nem de nosso interesse.


POLIMORFISMO
Os objetos-filhos herdam atributos e métodos de seus pais, mas, em algumas situações, é importante que ações para um mesmo método sejam diferentes. O polimorfismo ocorre quando existe uma alteração do funcionamento interno de um método herdado de um objeto-pai.

Exemplo

Vamos voltar a pensar no funcionamento da TV. O televisor pode ser um objeto que herda de uma classe chamada eletrodoméstico. Sabemos que todo eletrodoméstico pode ser ligado ou desligado, certo? Considerando dois objetos (uma TV e uma máquina de lavar roupa), ambos têm o método ligar e desligar, mas a forma como fazem isso é múltipla (polimorfismo).
'''

# Criação de Funções 

def printme (str):
    "Esta função vai imprimir: "
    print(str)
    return

printme("Entrada do Texto a ser impersso em tela.....")


#Criação  de classe 

class Empregado():
    contador = 0
    nome = ""
    salario = 0

    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario = salario
        Empregado.contador+= 1

    def mostra_contador (self):
        print ('Número de empregados: %d' % Empregado.contador)
        return
    
    def mostra_empregado (self):
        print ('Nome: ', self.nome, ", Salário: ", self.salario)
    

# Representaçaõ do ponto cartesiano Ponto Cartesiano 
class Ponto():    
    x = 0 
    y = 0
     
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def coordenadas(self):
        print("X = %s Y = %s " % (self.x, self.y))
        
        
empregado = Empregado(input('Digite o nome do empregado: '), 15.000)
pont = Ponto(5, 10)

empregado.mostra_contador()
empregado.mostra_empregado()

pont = Ponto(2,3)
pont.coordenadas()
pont = Ponto(3,2)
pont.coordenadas()


'''
Em vez de usar as instruções normais para acessar atributos, você também pode aplicar as seguintes funções:

getattr (objeto, nome [, default])

Para acessar o atributo do objeto


hasattr (objeto, nome)

Para verificar se existe um atributo ou não


setattr (objeto, nome, valor)

Para definir um atributo (se não existe, será criado)


delattr (objeto, nome)

Para excluir um atributo
'''