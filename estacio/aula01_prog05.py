n = nome = int(input("Quantos alunos a tuma tem ?\n ")) 

total = 0

for i in range(1, n+1):
	media = float(input(f"Digite  a média do {i}º alun: \n"))
	total = total+ media 

mediaTurma = total/n

print(f"A média da turma com {n} alunos foi {mediaTurma}")