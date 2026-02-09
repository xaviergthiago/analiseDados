numero = int(input("Digite o número: "))

def funcao_numero (num):
    if num  > 0:
        return "Número é positivo"
    
    elif num < 0:
        return "Número é negativo"
    
    else:
        return "Número é zero"

pos_neg_zero = funcao_numero (numero)
print(f"{pos_neg_zero}")