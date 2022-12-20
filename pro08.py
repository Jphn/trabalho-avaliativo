n1 = mdc = int(input('Nº 01: '))
n2 = int(input('Nº 02: '))

for mdc in range(n1, 0, -1):
    if (n1 % mdc == 0) and (n2 % mdc == 0):
        break

print(f'MDC{n1, n2} = {mdc}.')
