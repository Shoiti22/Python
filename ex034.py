salario = float(input('Digite Salario: '))
if salario <= 1250:
    aumento = (salario * 15 / 100) + salario
else:
    aumento = (salario * 10 / 100) + salario
print('Você Recebia R$ {:.2f} e agora Recebe {:.2f} Salario'.format(salario, aumento))