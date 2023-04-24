#ex 057 faça um programa que leia o sexo da pessoa e so aceite valores M e F
sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso.'.format(sexo))

#ex 058 Melhore o Jogo do Ex 028.