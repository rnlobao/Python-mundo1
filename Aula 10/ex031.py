viagem = float(input('Distancia de uma viagem em km: '))

if viagem < 200:
    preco = viagem * 0.5
else:
    preco = viagem * 0.45

print('O preço da viagem é: {}'.format(preco))