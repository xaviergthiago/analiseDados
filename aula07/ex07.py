
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

def funcao_maior_numero (numero1, numero2, numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2

    elif numero3 >= numero1 and numero3 >= numero2:
        return numero3

    else:
        return "Os número são iguais"

print(f"{funcao_maior_numero(n1, n2, n3)}")