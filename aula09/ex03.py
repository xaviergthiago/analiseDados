numeros = []
quantidade = int(input("Digite a quantidade de números: "))
for i in range(quantidade):
    numero = int(input(f"Digite o número {i+1}º número: ")) 
    numeros.append(numero) # Adiciona o número à lista
print(f"Números escolhidos: {numeros}")