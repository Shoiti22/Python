#emprestimo bancario.
print('\033[31mOlá eu sou seu assistente virtual e vou lhe ajudar no processo.\033[m')
casa = float(input('Qual o valor da casa ? R$ '))
salario = float(input('Qual o valor do seu salário ? '))
sltotal = salario * 30 / 100
anos = int(input('Quantos anos pretende pagar o financiamento ? '))
meses = anos * 12
prestaçao = casa / meses
if prestaçao <= sltotal:
    print('Seu Emprestimo de {:.2f} com a prestação de {:.2f} foi aceita.'.format(casa, prestaçao))
else:
    print('Para pagar uma casa de {:.2f} em {} anos a prestação sera de {:.2f} por mês foi negado.'.format(casa, anos, prestaçao))