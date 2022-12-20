n = int(input('Nº: '))

soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    msg = 'É'
else:
    msg = 'Não é'

print(f'{msg} perfeito.')
