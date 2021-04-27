nome = input('Digite seu nome completo: ')
nomemaisculo = nome.upper()
print(nomemaisculo)
nomeminusculo = nome.lower()
print(nomeminusculo)
espacos = nome.count(' ')
caracteres = len(nome) - espacos
print(caracteres)

nomeprimeiro = nome.split()
letrasnome1 = len(nomeprimeiro[0])
print(letrasnome1)
