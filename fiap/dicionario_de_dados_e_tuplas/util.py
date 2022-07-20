import os

def printMenuOptions():
    os.system('clear')
    op = input("O que deseja realizar ? \n" + 
              "<I> - Para Inserir um usuário\n" + 
              "<P> - Para Pesquisar um usuário\n" + 
              "<E> - Para Excluir um usuário\n" + 
              "<A> - Para Excluir um usuário\n" + 
              "<L> - Para Listar um usuário\n: ").upper()
    return op
#

def inserir(usuarios):
    login  = input("Digite seu login: ").upper()
    usuarios[login] = [input("Digite seu nome: ").upper(),
                 input("Digite a última data de acesso: ").upper(),
                 input("Qual a última estação acessada: ").upper()]
#

def alterar(usuarios):
    os.system('clear')
    login = input("\nDigite o Login do usuário:  ")
    for element in usuarios:
        if(login == element[0]):
            if input("\nDeseja alterar o nome: \"S\" ou \"N\"").upper() == "S":
                element[1] = input("Entre com o novo nome: ")
            if input("\nDeseja alterar a data do último acesso: \"S\" ou \"N\"").upper() == "S":
                element[1] = input("Entre com a última data: ")
            if input("\nDeseja alterar última sessão acessada").upper() == "S":
                element[1] = input("Entre com o nome da nova  estação: ")
#

def excluir(usuarios):
    os.system('clear')
    login = input("\nDigite o Login do usuário:  ")
    for element in usuarios:
        if(login == element[0]):
            usuarios[login].remove()
#

def pesquisar(usuarios):
    os.system('clear')
    login = input("\nDigite o Login do usuário: ")
    for element in usuarios:
        if(login == element[0]):
            print(usuarios[login])

#
