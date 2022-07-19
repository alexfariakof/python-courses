iventario = []
resposta = "S"

while resposta == "S":
    iventario.append(input("Equipamento: "))
    iventario.append(float(input("Valor: "))) #Erro será gerado caso a entrada seja diferete de número
    iventario.append(int(input("Número Serial: ")))
    iventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar ").upper()

for elemento in iventario:
    print(elemento)