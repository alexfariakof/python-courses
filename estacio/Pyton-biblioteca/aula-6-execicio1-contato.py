class Contato():
    todos_contatos = []
    nome = ""
    email = ""
    
    def __init__(self, _nome, _email):
        self.nome = _nome
        self.email = _email
        Contato.todos_contatos.append (self)

class Fornecedor(Contato):
    
    def pedido (self, pedido):
        print ("pedido %s feito por %s" % (pedido, self.nome))
        

class  Amigo(Contato):    
    telefone =  ""
    
    def __init__ (self, _nome, _email, telefone):
        super(). __init__ (_nome, _email)
        self.telefone = telefone
    
    def pedido (self):
        print ('Pedido do amigo ', self.nome,  'e seu email é ',   self.email, 'e seu telefone é ', self.telefone)

fornecedor = Fornecedor("Alex", "alex@gmail.com")
fornecedor.pedido("10 Hanburgueres")

amigo = Amigo("Izaide", "izaide@gmail.com", "99633-6565")
amigo.pedido()


'''
&__dict__	Dicionário que contém o espaço para nome da classe;
__doc__	Sequência de documentação de classe ou nenhuma (se indefinida);
__name__	Nome da classe;
__module__	Nome do módulo no qual a classe está definida (no modo interativo, esse atributo é “__main__”;
__bases__	Tupla possivelmente vazia que contém as classes-base na ordem de sua ocorrência e na lista correspondente
'''