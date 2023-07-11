from uteis import numeros

#Programa Principal.
num = int(input("Digite um valor."))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {numeros.dobro(num)}')