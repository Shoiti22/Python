palavras = ('aprender', 'estudar', 'linguagem', 'japones', 'python', 'curso')

for p in palavras:
    print(f'\nNa Palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')