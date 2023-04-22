#FuNÇÃO
def temp_F(temp_C):
    valor = (temp_C*9/5)+32
    return valor


#Procedimento
def temp_F(temp_C=25):
   valor = (temp_C*9/5)+32
   print("°C=",temp_C," °F=",valor)
temp_F()