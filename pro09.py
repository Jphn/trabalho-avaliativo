n = int(input('Nº: '))

i = 1

while i * (i + 1) * (i + 2) < n:
    i += 1

if i * (i + 1) * (i + 2) == n:
    msg = 'é'
else:
    msg = 'não é'

print(f'O número {n} {msg} triangular.')
