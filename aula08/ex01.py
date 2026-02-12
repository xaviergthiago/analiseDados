def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Não é possível dividir por zero."
    except ValueError:
        return "Valor inválido. Certifique-se de que ambos os argumentos sejam números."
    else:
        return resultado
    finally:
        print("Operação de divisão concluída.")
    
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(dividir(num1, num2))
except ValueError:
    print("Entrada inválida. Por favor, insira números válidos.")