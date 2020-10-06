from random import randint
valor = randint(1, 10)
chute = int(input('Chute um valor de 0 à 10: '))

while chute != valor:
    if chute > valor:
        chute = int(input('Chute um número mais baixo: '))
    else:
        chute = int(input('Chute um número mais alto: '))

print('Parabéns você acertou!')
