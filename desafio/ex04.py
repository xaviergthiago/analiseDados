num1 = int(input("Digite o valor do primeiro número: "))
num2 = int(input("Digite o valor do segundo número: "))
num3 = int(input("Digite o valor do terceiro número: "))

if num1>num2 and num1>num3:
    print(f"O maior número é {num1}")
elif num2>num1 and num2>num3:
    print(f"O maior número é {num2}")
elif num3>num1 and num3>num2:
    print(f"O maior número é {num3}")
else:
    print(f"Os número são iguais")