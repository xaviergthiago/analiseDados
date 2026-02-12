def buscar_produtos():
    produtos={"Sabão": 8.5, "Amaciante": 7.0, "Detergente": 9.2, "Água Sanitária": 3.8}
    try:
        produto = input("Digite o nome do produto: ").capitalize()
        quantidade = int(input("Digite a quantidade: "))
        preco_total = produtos[produto] * quantidade
    except KeyError:
        return "Produto não encontrado."
    except ValueError:
        return "Quantidade inválida."
    else:
        return f"O preço total de {quantidade} unidades de {produto} é: R${preco_total:.2f}"
    
print(buscar_produtos())