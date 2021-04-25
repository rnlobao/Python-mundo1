import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('Seno: {:.2f}\nCos: {:.2f}\nTg: {:.2f}'.format(seno, cosseno, tangente))
