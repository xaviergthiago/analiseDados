# Solicitar nome e idade de uma pessoa

def nome_idade(nome, idade):
    try:
        idade = int(idade)
    except ValueError:
        return "Idade inválida. Certifique-se de que seja um número inteiro." 
    return f"Nome: {nome}, Idade: {idade}"

name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

# Exibir as informações
print(nome_idade(name, age))