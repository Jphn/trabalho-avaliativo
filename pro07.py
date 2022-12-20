n1 = int(input('Nº 01: '))
n2 = int(input('Nº 02: '))

mmc = max(n1, n2)

while (mmc % n1 != 0) or (mmc % n2 != 0):
    mmc += 1

print(f'MMC{n1, n2} = {mmc}.')
