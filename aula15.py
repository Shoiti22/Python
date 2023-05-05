n = s = cont = 0
while n != 999:
    n = (int(input('Digite um numero digite 999 para parar')))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont} e somando da {s}')