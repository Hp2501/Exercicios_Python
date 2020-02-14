frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase[:-1]
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')
