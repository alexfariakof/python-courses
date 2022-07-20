# w - Abre arquivo para escrita
# r - Abre o arquivo para leitura
# a - Abre o arquivo para inserir novas informações 
# x - Abre o arquivo em modo exclusivo ou seja não pode se aberto enquanto não for fechado.

arquivo = open("arquivo01.txt", "w", encoding="**utf_8_sig**")
arquivo.write("Escrevendo conteúdo no meu arquivo!")
arquivo.close()

#segunda maneira e melhor forma de manipular arquivos

with open("arquivo01.txt", "a", encoding="**utf_8_sig**") as arquivo:
    arquivo.write("\nEstá é a melhor forma de manipular aqruivos com Python")