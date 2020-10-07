from time import sleep
from datetime import datetime

atual = datetime.now()
hora_atual = atual.hour
minuto_atual = atual.minute
segundo_atual = atual.second

print('HORÁRIO ATUAL')
print(f'{hora_atual} : {minuto_atual} : {segundo_atual}')

horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

while not horas == minutos == segundos == 0:
    print(f'{horas} : {minutos} : {segundos}')
    sleep(1)
    if minutos == segundos == 0:
        horas -= 1
        minutos = 59
        segundos = 59
    elif segundos == 0:
        minutos -= 1
        segundos = 59
    else:
        segundos -= 1

print('FIM')
