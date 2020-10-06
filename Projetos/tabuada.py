while True:
    n = int(input('Digite um número para ver a tabuada (-1 para parar): '))
    print('-' * 14)
    if n == -1:
        break
    for c in range(1, 11):
        print(f'{n}  X  {c} = {c * n}')
print('FIM.')
