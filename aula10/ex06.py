import pandas as pd

df = pd.read_csv("ClassicDisco.csv")

print("Primeiras Linhas do DataFrame:")
print(df.head())

print("Últimas Linhas do DataFrame:")
print(df.tail())