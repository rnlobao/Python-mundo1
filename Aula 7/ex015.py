km = float(input('Quantos km percorridos? '))
dias = int(input('Quantos dias foram alugados? '))
preco = (60 * dias) + (0.15 * km)
print('Esse foi o preço: {:.2f}'.format(preco))