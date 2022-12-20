import math

n = int(input('Nº: '))

x = (math.sqrt((8 * n + 1)) + 1) / 4

if (x >= 0) and (x == int(x)):
    msg = 'É'
else:
    msg = 'Não é'

print(f'{msg} hexagonal.')
