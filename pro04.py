n = int(input("Digite o valor de n : "))

z = k = 1

i = int(input("Digite o valor de i(para ser o múltiplo): "))
j = int(input("Digite o valor de j(para ser o múltiplo): "))

while z <= n:

    if k % i == 0 and k % j == 0:
        print(k, end=',')
        z += 1
    elif k % i == 0:
        print(k, end=',')
        z += 1
    elif k % j == 0:
        print(k, end=',')
        z += 1

    k += 1
