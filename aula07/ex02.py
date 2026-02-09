media_aluno = int(input("Digite a média: "))

def funcao_media (media):
    if media  >= 7:
        return "Aprovado"
    
    elif media >= 5:
        return "Recuperação"
    
    else:
        return "Reprovado"

aprovado_reprovado_recuperacao = funcao_media (media_aluno)
print(f"{aprovado_reprovado_recuperacao}")