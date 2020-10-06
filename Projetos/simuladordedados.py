from random import randint
dado1 = randint(1, 6)
dado2 = randint(1, 6)
maior = 0
menor = 7
soma = dado1 + dado2

#Verificar qual é o maior valor
if dado1 > maior:
    maior = dado1
if dado2 > dado1:
    maior = dado2

#Verificar qual foi o menor valor
if dado1 < menor:
    menor = dado1
if dado2 < dado1:
    menor = dado2

print(f'O dado 1 conseguiu {dado1};')
print(f'O dado 2 conseguiu {dado2};')
print(f'O maior valor foi {maior};')
print(f'O menor valor foi {menor};')
print(f'A soma dos valores é {soma}')