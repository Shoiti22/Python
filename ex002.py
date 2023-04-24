nome = input('Qual é seu nome?')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
print('É um prazer te conhecer {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
