from datetime import date

def voto(a):
    atual = date.today().year
    idade = atual-a
    if atual-a >= 18 and atual-a <= 65:
        return (f'Voto Obrigario pois você tem {idade} Anos')
    elif atual-a <= 16:
        return (f'Não Precisa votar pois você tem {idade} Anos.')
    else:
        return (f'Voto Opcional pois você tem {idade} Anos')


#Programa Principal
ano = int(input('Que Ano Você Nasceu? '))
print(voto(ano))