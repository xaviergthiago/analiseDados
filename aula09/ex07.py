dados = ("Maria", 25)
print(f"1ª versão da tupla: {dados}")
novoValor = input("Profissão: ")
dados = dados + (novoValor,)  # Adiciona o novo valor à tupla
print(f"2ª versão da tupla: {dados}")