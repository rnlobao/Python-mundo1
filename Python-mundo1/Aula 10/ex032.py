ano = int(input('Digite um ano: '))

if (ano % 4) == 0:
    if (ano % 100) == 0:
        if (ano % 400) == 0:
            print('Ele é bissexto')
        else:
            print('Nao é bissexto')
    else:
        print('Ele é bissexto')
else:
    print('Nao é bissexto')