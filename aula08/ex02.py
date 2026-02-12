try:
    numero = int(input("Digite um número: "))
    print(f"Número convertido com sucesso: {numero}")
except ValueError:
    print("Erro: O valor digitado não é numérico!")