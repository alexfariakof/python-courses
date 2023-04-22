class Pessoa:
       def __init__(self, nome ='', idade=0):
              self.nome = nome
              self.idade = idade
       def getIdade(self):
              return self.idade

class PessoaFisica(Pessoa):
       def __init__(self, CPF, nome='', idade=0):
              Pessoa.__init__(self, nome, idade)
              self.CPF = CPF

class PessoaJuridica(Pessoa):
       def __init__(self, CNPJ, nome='', idade=0):
              Pessoa.__init__(self, nome, idade)
              self.CNPJ = CNPJ
              
       def getPessoa(self):
              print('{} tem {} de idade'.format(self.nome, self.idade))


pf = PessoaFisica("095.000.666-89", "Alex", 39)              
pj = PessoaJuridica("66546546546546454654", "Izaide", 50)

pf.getIdade()
pj.getPessoa()
