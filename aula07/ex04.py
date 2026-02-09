numero = int(input("Digite o número: "))

def funcao_numero (num):
    if num  %2 == 0:
        return "Número é par"
    
    else:
        return "Número é ímpar"

par_impar = funcao_numero (numero)
print(f"{par_impar}")