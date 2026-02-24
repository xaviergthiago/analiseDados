#o usuário escolhe 5 nomes :
nomes = set()  # Cria um conjunto vazio para armazenar os nomes
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.add(nome)  # Adiciona o nome ao conjunto

print(f"Nomes escolhidos: {nomes}")
for nome in nomes:
    print(nome)