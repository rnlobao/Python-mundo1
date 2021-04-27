a = int(input('Comprimento da reta 1: '))
b = int(input('Comprimento da reta 2: '))
c = int(input('Comprimento da reta 3: '))

d = abs(b-c)
e = abs(a-c)
f = abs(a-b)

if (d < a) and (a < (b+c)):
    j1 = 1
else:
    j1 = 2

if (e < b) and (b < (a+c)):
    j2 = 1
else:
    j2 = 2

if (f < c) and (c < (a+b)):
    j3 = 1
else:
    j3 = 2

j = j1+j2+j3

if j == 3:
    print('Esse triangulo existe')
else:
    print('Esse triangulo NAO existe')
