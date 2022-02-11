nome = input('Digite seu nome: ')
santo = nome.find('silva')

if santo == -1:
    print('Nao tem silva')
else:
    print('tem silva')