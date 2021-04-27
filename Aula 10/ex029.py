vel = float(input('Qual a velocidade do carro: '))

if vel > 80.0:
    multa = (vel - 80.0) * 7.0
    print('Voce foi multado em {} reais!'.format(multa))

