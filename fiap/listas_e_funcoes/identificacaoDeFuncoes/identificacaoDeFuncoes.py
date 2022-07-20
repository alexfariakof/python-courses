def preencherIventario(lista):
    resp = "S"
    while resp == "S":
        equipamento=[input("Equipamento: "), 
                      float(input("Valor: ")),
                      int(input("Número Serial: ")),
                      input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()
#

def exibirIventario(lista):
    for element in lista:
        print("Nome..........: ", element[0])
        print("Valor.........: ", element[1])
        print("Serial........: ", element[2])
        print("Departamento..: ", element[3])
#

def localizarPorNome(lista):
    busca  = input("\nDigite o nome do equipamento que deseja buscar:  ")
    for element in lista:
        if busca == element[0]:
            print("Valor.....:", element[1])
            print("Serial....:", element[2])
#

def depreciacaoPorNome(lista):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado:  ")
    for element in lista:
        if(depreciacao == element[0]):
            print("Valor antigo: ", element[1])
            element[1] = element[1] * (1-porc/100)
            print("Novo valor: ", element[1])
#

def excluirPorSerial(lista):
    serial = int("Digite o serial do equipamento que será excluido: ")
    for element in lista:
        if element[2] == serial:
            lista.remove(element)
    return "Item excluído."
#

def resumirValores(lista):
    valores = []
    for element in lista:
        valores.append(element[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
#