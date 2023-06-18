def escreva(txt):
    t = len(txt)+4
    print('-' * t)
    print(f'{txt:^{t}}')
    print('-' * t)

#Program Principal.
escreva('Oi')
escreva('Maneiro mewwwww')