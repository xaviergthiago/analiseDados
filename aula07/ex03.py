idade_ingresso = int(input("Digite a idade: "))

def funcao_ingresso (idade):
    if idade  < 12:
        return "R$10,00"
    
    elif idade <= 18:
        return "R$15,00"
    
    else:
        return "R$20,00"

preco_ingresso = funcao_ingresso (idade_ingresso)
print(f"{preco_ingresso}")