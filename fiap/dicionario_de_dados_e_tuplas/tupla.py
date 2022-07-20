usuarios = {} # é uma lista 
emails = ["xpto@gmail.com", "otpx@tim.com.br"] # é um dicionario

tupla = list(enumerate(emails)) # é uma tupla

print(tupla)

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]

for chave, dado in usuarios.items():
    print("Usuário..: ", chave[0])
    print("Email....:", chave[1])
    print("Nome.....:", dado[0])
    print("Nível....:", dado[1])