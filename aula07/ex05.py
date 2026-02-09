faixa_etaria = int(input("Digite a idade: "))

def funcao_faixa_etaria (idade):
    if idade  < 13:
        return "Criança"
    
    elif idade < 18:
        return "Adolescente"
    
    elif idade < 60:
        return "Adulto"
    
    else:
        return "Melhor idade"

print(f"{funcao_faixa_etaria(faixa_etaria)}")