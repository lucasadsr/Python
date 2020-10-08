import random
from time import sleep
escolha = int(input('''ESCOLHA UMA DAS OPÇÕES
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
'''))
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
escolhapc = random.choice(opcoes)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if escolha == 1:
    if escolhapc == 'PEDRA':
        print(f'Você escolheu PEDRA e o computador {escolhapc}')
        print('EMPATE')
    elif escolhapc == 'PAPEL':
        print(f'Você escolheu PEDRA e o computador {escolhapc}')
        print('VOCÊ PERDEU')
    else:
        print(f'Você escolheu PEDRA e o computador {escolhapc}')
        print('VOCÊ GANHOU')

if escolha == 2:
    if escolhapc == 'PAPEL':
        print(f'Você escolheu PAPEL e o computador {escolhapc}')
        print('EMPATE')
    elif escolhapc == 'TESOURA':
        print(f'Você escolheu PAPEL e o computador {escolhapc}')
        print('VOCÊ PERDEU')
    else:
        print(f'Você escolheu PAPEL e o computador {escolhapc}')
        print('VOCÊ GANHOU')

if escolha == 3:
    if escolhapc == 'TESOURA':
        print(f'Você escolheu TESOURA e o computador {escolhapc}')
        print('EMPATE')
    elif escolhapc == 'PEDRA':
        print(f'Você escolheu TESOURA e o computador {escolhapc}')
        print('VOCÊ PERDEU')
    else:
        print(f'Você escolheu TESOURA e o computador {escolhapc}')
        print('VOCÊ GANHOU')
