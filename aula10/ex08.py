import pandas as pd
df = pd.read_excel("bancos.xlsx")
#print(df.to_string()) #Exibe o DataFrame completo, sem truncar as linhas ou colunas.
#print(df["Banco"])
x = df["Banco"].value_counts()
print(x)