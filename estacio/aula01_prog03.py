nome = input("Qual o seu nome ? ") 
idade = int(input("Qual a sua idade ? "))

print(f"O usuário {nome} possui {idade} anos")
 
if idade >= 18:
	print(f"{nome} está apto a tirar CNH.")
else:
	print(f"{nome} não está apto a tirar CNH.")