l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

# Verifica se o triângujo pode ser formado e informa seu tipo
if (l1 > l2 + l3) or (l2 > l1 + l3) or (l3 > l2 + l1):
    print(f'O triângulo de lados {l1}, {l2} e {l3} não pode ser formado.')
else:
    print(f'O triângulo de lados {l1}, {l2} e {l3} pode ser formado.')
    if l1 == l2 == l3:
        print('O triângulo é EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo é ISÓSCELES')
    else:
        print('O triângulo é ESCALENO')
