frase = str(input('Digite uma frase ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é  {}'.format(junto, inverso))
if inverso == junto:
    print('Ele é Palindromo')
else:
    print('Não é Palindromo')