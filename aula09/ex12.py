alunos = {}
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    alunos[nome] = input("Digite as notas do aluno (separadas por vírgula): ").split(",")  # Adiciona o nome e as notas ao dicionário
# Calcula a média das notas para cada aluno
for nome, notas in alunos.items(): # Itera sobre os alunos e suas respectivas notas
    notas = [float(nota) for nota in notas]  # Converte as notas para float
    media = sum(notas) / len(notas)  # Calcula a média das notas
    alunos[nome] = {"notas": {"nota1": notas[0], "nota2": notas[1], "nota3": notas[2], "media": media}}  # Atualiza o dicionário com as notas e a média
print(f"Dicionário: {alunos}")