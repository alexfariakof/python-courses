a = open('c:\\Users\\alexf\\Documents\\ESTACIO 2023.1 PYTON\\teste.py','r')
print(a)
    
# e - Abre o arquivo apenas para leitura (read). Você não pode inserir ou modificar o conteúdo.
# w - Abre o arquivo apenas para escrita. O arquivo que existia será sobrescrito pelo atual.
# a – append - Abre o arquivo para inserção de dados que serão escritos no final do arquivo.
# r+ - Abre o arquivo para leitura e escrita.

#ITERAR EM UM ARQUIV
for linha in a:
     print(linha)

#LER TODAS AS LINHAS DE UM ARQUIVO
a = open('c:\\Users\\alexf\\Documents\\ESTACIO 2023.1 PYTON\\teste.py','r')
conteudo = a.read()
print(conteudo)

#LER TODAS AS LINHAS EM UMA LISTA

a = open("c:\\users\\fabiano\\ajax_info.txt")
lin1 = a.readline()
lin2 = a.readline()
print(lin1)
print(lin2)

#LER O ARQUIVO LINHA POR LINHA

#CRIAR UM ARQUIVO VAZIO

#APAGAR O CONTEÚDO DE UM ARQUIVO

#ESCREVER EM UM ARQUIVO-TEXTO

#ADICIONAR MAIS CONTEÚDO AO ARQUIVO EXISTENTE