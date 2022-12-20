n = int(input('Nº: '))

c = 0

for i in range(1, n + 1):
    if n % i == 0:
        c += 1

if c == 2:
    msg = 'É'
else:
    msg = 'Não é'

print(f'{msg} primo.')
