import math
angulo = float(input('Digite um Angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O Angulo {} de seno {:.2f}'.format(angulo, seno))
print('O Angulo {} de cosseno {:.2f}'.format(angulo, cosseno))
print('O Angulo {} de tangente {:.2f}'.format(angulo, tangente))