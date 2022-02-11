nome = input('Digite o nome de uma cidade: ')
nomesplitado = nome.split()
santo = nomesplitado[0].find('santo')

if santo == -1:
    print('Nao tem santo')
else:
    print('tem santo')