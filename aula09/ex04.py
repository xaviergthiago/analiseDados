aluno = 1
while aluno<=10:
    print(f"Aluno {aluno}")
    notas = []
    nome = input("Digite o nome do aluno: ")
    for i in range(3):
        nota = int(input(f"Digite a nota {i+1} do aluno {nome}: ")) 
        notas.append(nota) # Adiciona o número à lista
    media = sum(notas) / len(notas)
    print(f"Notas do aluno {nome}: {notas}")
    #print(f"A média do aluno {nome} é: {media:.2f}")
    print(f"A média do aluno {nome} é:", round(media, 2))
    if media >= 7:
        print(f"O aluno {nome} foi aprovado!")
    elif media >= 5:
        print(f"O aluno {nome} está de recuperação!")
    else:
        print(f"O aluno {nome} foi reprovado!")
    #print(f"Números escolhidos: {numeros}")

    aluno += 1