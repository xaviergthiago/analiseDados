nota_conceito = int(input("Digite a nota: "))

def funcao_nota_conceito (nota):
    if nota >= 9:
        return "A"
    
    elif nota >= 7:
        return "B"
    
    elif nota >= 5:
        return "C"
    
    else:
        return "D"

print(f"{funcao_nota_conceito(nota_conceito)}")