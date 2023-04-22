#Módulo é um arquivo que contém código Python, no qual é possível 
# encontrar definições de classes, funções ou até sequência de comandos. 
# Normalmente, há uma extensão .py associada a esse arquivo.


# arquivo: transportes.py
def calcula_frete():
       #código da função
def calcula_imposto():
       #código da função
def distancia():
       #código da função
       

#importamando arquivo
import transportes
# neste caso estamos importando TUDO que estiver dentro do módulo

from transportes import distancia
# neste caso, do módulo transportes.py só vamos importar a função distancia(), as outra
# não serão importadas

from transportes import *
# neste caso, importa tudo que estiver no módulo


'''
Este exemplo é bem autoexplicativos, mas há um detalhe na última 
forma de importação: quando usamos o símbolo do asterisco (“*”), 
tudo o que foi definido dentro do módulo será importado, EXCETO 
os nomes que começam com o caractere underline (“_”). Não é muito comum usar o asterisco (“*”).

Aprenda, a seguir, a aplicar a função de um módulo:
'''
transportes.distancia()
# coloque o nome do módulo e o recurso que deseja
# também é possível atribuir uma variável, assim:
dist = transportes.distancia()
dist

#Para saber os nomes que existem dentro de um módulo, use a função dir():

