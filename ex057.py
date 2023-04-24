sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso.'.format(sexo))