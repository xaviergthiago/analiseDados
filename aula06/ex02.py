def imc (peso,altura):
    return peso/(altura*altura)

def classificacao(imc):
    if imc < 16.9:
        return "Muito abaixo do peso"
    
    elif 17 < imc <= 18.4:
        return "Abaixo do peso"
    
    elif 18.5 < imc <= 24.9:
        return "Peso normal"
    
    elif 25 < imc <= 29.9:
        return "Acima do peso"
    
    elif 30 < imc <= 34.9:
        return "Obesidade Grau I"
    
    elif 35 < imc <= 40:
        return "Obesidade Grau II"

    elif imc > 40:
        return "Obesidade Grau III"

print("Programa Principal\n")
peso_usuario = float(input("Peso: ").replace(",","."))
altura_usuario = float(input("Altura: ").replace(",","."))

imc_calculo = imc(peso_usuario,altura_usuario) #injeção da função somar
classificacao_imc = classificacao(imc_calculo)

print(f"IMC: {imc_calculo:.2f}".replace(".",","))
print(f"Classificação: {classificacao_imc}")