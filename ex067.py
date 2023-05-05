while True:
    n = int(input('QUER VER A TABUADA QUAL VALOR? '))
    if n < 0:
        break
    print('---' * 20)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('ACABOU ')