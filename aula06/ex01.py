def somar (a,b):
    return a + b

def subtrair (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def dividir (a,b):
    if b!=0:
        return a / b
    else:
        return "Erro: divisão por zero!"
        
def media (a,b):
    return (a + b)/2

print("Programa Principal\n")
num1 = int(input("1º valor: "))
num2 = int(input("2º valor: "))

soma = somar(num1,num2) #injeção da função somar
subtracao = subtrair(num1,num2)
multiplicacao = multiplicar(num1,num2)
divisao = dividir(num1,num2)
media = media(num1,num2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Média: {media}")