numero = input('Digite um nome de 0 a 9999: ')
carac = len(numero)
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(unidade, dezena, centena, milhar))

#duvidas!