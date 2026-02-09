nome = (input("Nome: "))
salarioBruto = float(input("Salário Bruto: "))

def inss (salarioBruto):
    if salarioBruto >= 1800:
        return 0.11*salarioBruto
    
    elif salarioBruto < 1800:
        return 0.09*salarioBruto

def vt (salarioBruto):
    if salarioBruto >= 1500:
        return 0.06*salarioBruto
    
    elif salarioBruto < 1500:
        return 0.05*salarioBruto

def bonus (salarioBruto):
    if salarioBruto >= 1240:
        return 700
    
    elif salarioBruto < 1240:
        return 500

def cargo (salarioBruto):
    if salarioBruto >= 3000:
        return "Acionista"
    
    elif salarioBruto >= 2000:
        return "Gerente"

    elif salarioBruto < 2000:
        return "Vendedor"

def salarioLiquido (salarioBruto, inss, vt, bonus):
    return salarioBruto - inss - vt + bonus

print("Programa Principal\n")
#salario_bruto = float(input("Salário Bruto: "))

inss_ = inss (salarioBruto)
vale_transporte = vt (salarioBruto)
bonus_ = bonus (salarioBruto)
cargo_ = cargo (salarioBruto)
salario_liquido = salarioLiquido (salarioBruto, inss_, vale_transporte, bonus_)

print(f"Nome: {nome}")
print(f"Salário Bruto: {salarioBruto}")
print(f"INSS: {inss_}")
print(f"Vale Transporte: {vale_transporte}")
print(f"Bônus: {bonus_}")
print(f"Cargo: {cargo_}")
print(f"Salário Líquido: {salario_liquido}")