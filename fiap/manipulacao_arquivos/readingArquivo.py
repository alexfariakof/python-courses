with open("iris.csv", "r", encoding="**utf_8_sig**") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("iris.csv", "r", encoding="**utf_8_sig**") as arquivo:
     for linha in arquivo.readlines():
        print(linha)