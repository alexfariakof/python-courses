x = input("Entre com o seu nome : ")
print(x)
i = 0
while i <= 2:
    if i == 0:
        print("0")
        print("Primeiro inteiração do while")
    else: 
        if i == 2:
            print(i)
            print("Terceira interação do while")
        print(i)
    i = i + 1
if x == "alex":
    print("Fim do interção com While " + x)

tabuada = int(input("Digite o numero para ver a tabuada:"))
for valor in range(1, 11, 1):
    print(str(tabuada) + " X " + str(valor) + " = " + str(tabuada*valor))

