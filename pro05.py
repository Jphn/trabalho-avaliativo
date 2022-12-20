i = int(input('Nº: '))
m = int(input('M: '))
j = int(input('J: '))

res = ''

for k in range(1, i + 1):
    if (k % m) == (j % m):
        res += f'{k}'
        res += ', ' if k != i else '.'

print(res)
