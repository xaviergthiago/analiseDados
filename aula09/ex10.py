pessoas = {}
for i in range(4):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    pessoas[nome] = idade # Adiciona o nome e a idade ao dicionário

print(f"Dicionário: {pessoas}")