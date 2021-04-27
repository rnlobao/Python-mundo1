#fatiamento de uma cadeia de strings
frase = 'curso em video python'
print(frase[9])
#isso vai printar a letra v, ou o item 9 na cadeia de strings

print(frase[9:13])
#vai printar do 9 ao 12
print(frase[9:14])

print(frase[9:21:2])
#nessa situação vai printar ate o 21 a partir do 9, pulando de 2 em 2

print(frase[:5])
#vai começar do caracter 0 e printar ate o 4 (5-1)

print(frase[15:])
#15 ate o final

print(frase[9::3])
#printa do 9 ate o final pulando de 3 em 3

tamanho = len(frase)
print(tamanho)
#isso printa quantos quadradinhos a frase ocupa

numo = frase.count('o')
print(numo)
#isso conta quantas vezes tem a letra 'o'

numo2 = frase.count('o', 0, 13)
print(numo2)
#printa quantas vezes aparece a letra "o" entre os caracteres 0 e 12

ondeesta = frase.find('deo')
print(ondeesta)
#vai mostrar em que posição começa o deo nos quadrinhos
#Se o find retornar -1 significa que nao achou

booleano = 'curso' in frase
print(booleano)
#vai mostrar com V ou F se tem a palavra desejada

novafrase = frase.replace('python', 'Android')
print(novafrase)
#substitui por android a palavra python

emmaiusculo = frase.upper()
print(emmaiusculo)
#frase.upper() vai deixar em maiusculo
#frase.lower() deixa tudo em minusculo

#frase.capitalize() vai deixar a primeira em maiuscula [0] e TODAS as outras em minusculo
#frase.title() transforma todo começo de palavra em letra maiuscula
#frase.strip() tira caracteres inutilizados do começo e do fim ou seja barras de espaço
#frase.rstrip() tira caracteres inutilizados do fim ou seja barras de espaço
#frase.lstrip() tira caracteres inutilizados do começo ou seja barras de espaço

#frase.split() divide uma string em varias palavras que formam uma lista
#'-'.join(frase) junta toda a frase e separa elas por -