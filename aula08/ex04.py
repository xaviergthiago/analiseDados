def somar (a,b):
    resultado = a + b
    return resultado

def subtrair (a,b):
    resultado = a - b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Não é possível dividir por zero."
    
    else:
        return resultado
        
def media (a,b):
    return (a + b)/2

try:
    opcao = int(input("Escolha a operação: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    match opcao:
        case 1:
            print(f"A soma é: {somar(num1, num2)}")
        case 2:
            print(f"A subtração é: {subtrair(num1, num2)}")
        case 3:
            print(f"A multiplicação é: {multiplicar(num1, num2)}")
        case 4:
            print(dividir(num1, num2))    
except ValueError:
        print("Valor inválido. Certifique-se de que ambos os argumentos sejam números.")
finally:
    print("Operação concluída.")