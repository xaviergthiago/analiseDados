import pandas as pd

dados = {
    'cargos':["Analista", "Assistente", "Gerente", "Diretor"],
    'salarios':[1000, 2000, 3000, 4000]
}

dados_resutado = pd.DataFrame(dados)
dados_resutado.index = dados_resutado.index + 1
print(dados_resutado)