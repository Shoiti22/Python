'''co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Comprimento do Oposto:'))
ca = float(input('Comprimento do Adjacente: '))
hi = math.hypot(co, ca)
print ('A Hipotenusa vai medir {:.2f}'.format(hi))