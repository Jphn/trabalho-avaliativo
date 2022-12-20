n = int(input('Nº: '))

i = 1

while True:
    p = (3 * i * i - i) / 2

    i += 1

    if p >= n:
        break

if p == n:
    msg = 'É'
else:
    msg = 'Não é'

print(f'{msg} pentagonal.')
