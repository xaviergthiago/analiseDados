salarioBruto = float(input("Digite o valor do salário: ").replace(",","."))

if salarioBruto>=5000:
    desconto = 0.14

elif salarioBruto>=4000:
    desconto = 0.12

elif salarioBruto>=2000:
    desconto = 0.11

else:
    desconto = 0.09

salarioFinal = salarioBruto - salarioBruto*desconto

print(f"O salário líquido é {salarioFinal:.2f}".replace(".", ","))