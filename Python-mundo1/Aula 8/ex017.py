from math import sqrt, pow
op = float(input('Cateto oposto: '))
adj = float(input('Cateto adj: '))
h = sqrt((pow(adj, 2)) + (pow(op, 2)))
print('Hipotenusa: {:.2f}'.format(h))
