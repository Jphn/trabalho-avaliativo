import math

n = int(input('Nº: '))

raiz = math.sqrt(n)

if raiz == int(raiz):
    res = 'É '
else:
    res = 'Não é'

print(f'{res} um quadrado perfeito.')
