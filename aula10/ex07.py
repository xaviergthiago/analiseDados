#Filtrar músicas lançadas após 1980
import pandas as pd

df = pd.read_csv("ClassicDisco.csv")

filtro = df[df["Year"] > 1980]

print(filtro.to_string())

#Acrescente no final o ano e amúsica (track)
filtro_com_ano_e_musica = df[df["Year"] > 1980][["Year", "Track"]]