expr = str(input('Digite a Expressão: '))
pilha = list()
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua espressão esta valida.')
else:
    print('Sua espressão esta errada.')