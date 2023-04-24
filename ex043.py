print('Calculando seu IMC por favor responda abaixo.')
print('==' * 20)
peso = float(input('Qual o seu peso? (KG) '))
altura = float(input('Qual a sua Altura? (M) '))
imc = peso / (altura * altura)
print('\033[34mO Seu IMC é {:.1f}\033[m'.format(imc))
if imc <= 18.5:
    print('\033[36mAbaixo do Peso!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal.\033[m')
elif 25 <= imc < 30:
    print('\033[33mSobre Peso tome cuidado!\033[m')
elif 30 <= imc < 40:
    print('\033[31mVocê esta com Obesidade! \033[m')
else:
    print('\033[31mVocê esta com Obecidade Morbida! \033[m')