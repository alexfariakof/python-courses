import json

with open("arquivo.json", "r") as arquivoJson:
    dic = json.load(arquivoJson)
    for chave, valor in dic.items():
        print(chave + " " + str(valor))


dicionario = {"Seu Madruga": ["Madruguinha ", "31/12/2022", "Patio"],
              "Chiquinha": ["Chuiquinha Pintadinha", "30/12/2022", "Patio_02"],
              "Seu Barriga": ["Barriga", "01/12/2022", "Casa_171"]}

with open("jsonNovo.json", "w") as _json:
    json.dump(dicionario, _json)

        