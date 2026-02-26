import pandas as pd
cargos =[]
salarios = []
qtd = int(input("Quantos funcionários quer testar? "))
for i in range(qtd):
    print(f"Cadastro nº{i+1}")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    cargos.append(cargo)
    salarios.append(salario)

dados = {'cargos': cargos, 'salarios': salarios}
df=pd.DataFrame(dados)

print("\nTabela de cargos e salários\n")
print(df)