import math

n = int(input('Nº: '))

x = (math.sqrt((24 * n + 1)) + 1) / 6

if (x == int(x)):
    msg = 'É'
else:
    msg = 'Não é'

print(f'{msg} pentagonal.')
