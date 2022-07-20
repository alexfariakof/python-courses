from ControlUser import *
usuarios = {}
opcao = printMenuOptions()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "A" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios)
    if opcao == "E":
        excluir(usuarios)
    if opcao == "A":
        alterar(usuarios)

    opcao = printMenuOptions()
