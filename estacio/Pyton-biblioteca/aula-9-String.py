str1 = "Nabucodonosor" 

#Acessar os caracteres da string por seu índicestr1 = "Nabucodonosor"
str1 #'Nabucodonosor'
[str1[0]] #'N'
str1[1] #'a'
str[20]

#Iterar em strings
for i in str1:
        print(i)
        
        
#Você também pode fatiar (slice) a string:str1[0:5]
str1[:5] #['Nabuc']
str1[5:] #'odonosor'


#Verificar se um caractere está na string
'f' in str1 #False
'n' in str1 #True

#Identificar o tamanho da string
len(str1)

#Converter a string para maiúsculas ou minúsculas
str1.upper() #'NABUCODONOSOR'
str1.lower() #'nabucodonosor'


#Converter um número para uma string
x = 666
type(x) #<class 'int'>
x1 = str(x)
type(x1) #<class 'str'>


#Verificar se a string contém caracteres não alfabéticos
str1.isalpha() #True
str1="Nabucodonosor123"
str1.isalpha() #False

#Retirar espaços em branco no início e no fim da string
str2 = " Nabucodonosor "
str2 #' Nabucodonosor '
str2.strip() #'Nabucodonosor'

#Juntar cada item da string por meio de um delimitador especificado
str2 #'Nabucodonosor'
"-".join(str2) #'N-a-b-u-c-o-d-o-n-o-s-o-r'
