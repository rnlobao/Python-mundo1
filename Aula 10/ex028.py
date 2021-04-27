import random
num = random.randint(0, 5)

num2 = int(input('Adivinhe um numero de 1 a 5: '))
if num2 == num:
    print('Voce acertou!')
else:
    print('Voce errou o numero certo era {}!'.format(num))