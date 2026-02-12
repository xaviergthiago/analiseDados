def buscar_alunos():
    alunos={"Ana": 8.5, "Bruno": 7.0, "Carlos": 9.2}
    try:
        nome = input("Digite o nome do aluno: ").capitalize()
        nota = alunos[nome]
    except KeyError:
        return "Aluno não encontrado."
    else:
        return f"A nota de {nome} é: {nota}"
    
print(buscar_alunos())