from identificacaoDeFuncoes import *

minhaLista = []
print("Preenchimento")
preencherIventario(minhaLista)
print("Exibindo")
exibirIventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando \"Depreciação do Valor\"")
depreciacaoPorNome(minhaLista)

print("Exluindo")
excluirPorSerial(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
