nome = input("Qual o seu nome ? ") 

av1 = float(input("\nEntre com a nota da AV1: "))
av2 = float(input("\nEntre com a nota da AV2: "))

media = (av1+av2)/2

if media >= 7:
	print(f"O aluno {nome} está aprovado com média {media}")
elif media >=4:
	print(f"O aluno {nome} está em exame final com média {media}")
else:
	print(f"O aluno {nome} está reprovado com média {media}")