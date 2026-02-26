import pandas as pd

df = pd.read_csv("ClassicDisco.csv")

#print(df)
#print(df.to_string()) #Exibe o DataFrame completo, sem truncar as linhas ou colunas.
print(df.head()) #Exibe as primeiras 5 linhas do DataFrame.