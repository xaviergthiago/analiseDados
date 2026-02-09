valor_produto = int(input("Digite o valor do produto: "))

def funcao_desconto_produto (valor):
    if valor >= 500:
        desconto = 0.09
    
    elif valor >= 200:
        desconto = 0.08

    else:
        desconto = 0.07
    
    valor_final = valor * (1 - desconto)

    return (
        f"Desconto aplicado: {int(desconto * 100)}%\n"
        f"Valor final: R$ {valor_final:.2f}"
        )

print (funcao_desconto_produto(valor_produto))
#print (f"{valor_produto} com desconto fica {funcao_desconto_produto(valor_produto)}")