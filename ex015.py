d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos KM rodados? '))
a = (d * 60)
km = (k * 0.15)
sum = a+km
#pago = (dias * 60) + (km * 0.15)
t = print('total a pagar é por dia R$ {:.2f} e por km R$ {:.2f} total a pagar R$ {:.2f}'.format(a, km, sum))