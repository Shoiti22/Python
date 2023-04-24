from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento : '))
print('[1]MASCULINO')
print('[2]FEMININO')
sexo = int(input('Qual Sexo ?'))
idade = atual - nasc
print('Quem Nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18 and sexo == 1:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade > 18 and sexo == 1:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos. '.format(saldo))
    ano = atual - saldo
    print('Seu Alistamento foi no ano {}'.format(ano))
elif idade < 18 and sexo == 1:
    saldo = 18 - idade
    print('Ainda falta {} Anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu Alistamento sera no ano {}'.format(ano))
elif sexo == 2:
    print('Mulheres não precisa prestar serviço militar.')