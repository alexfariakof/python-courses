usuarios = {}
usuarios = {"Chaves":["Chaves do 8 ", "24/12/2022", "Cozinha_01"],
       "Quico":["Quico das Flores", "20/12/2022", "Enfermaria_05"]}

print(usuarios)

usuarios["Florinda"] = ["Dona Florinda", "21/12/2022", "Enfermaria_05"]
print(usuarios)

print(usuarios.get("Quico"))