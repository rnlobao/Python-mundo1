salario = float(input('Qual seu salario: '))
if salario > 1250.0:
    print('Salario ajustado: {}'.format(salario * 1.1))

else:
    print('Salario ajustado: {}'.format(salario * 1.15))