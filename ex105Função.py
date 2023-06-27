def notas(*n, sit=False):
    """
    -> função para analisar notas dos alunos
    :param n: uma ou mais notas.
    :param sit: valor opcional
    :return: dicionario com varias situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal.
resp = notas(2, 1, 5.5, 2.5, 8.5)
print(resp)