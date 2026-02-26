import pandas as pd

df = pd.read_csv("ClassicDisco.csv")

#filtro = df["Artist"] == "Aretha Franklin" #Filtra as linhas onde a coluna "Artist" é igual a "Aretha Franklin".
filtro = df[df["Artist"] == "Aretha Franklin"]["Artist"] #Filtra as linhas onde a coluna "Artist" é igual a "Aretha Franklin" e exibe apenas a coluna "Artist".

print(filtro.to_string())