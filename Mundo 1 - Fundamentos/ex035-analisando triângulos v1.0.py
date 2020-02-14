print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)
ps = float(input('Primeiro segmento: '))
ss = float(input('Segundo segmento: '))
ts = float(input('Terceiro segmento: '))
if ps < ss + ts and ss < ps + ts and ts < ss + ps:
    print('Os segmentos acima, SIM formam um triângulo ')
else:
    print('Os segmentos acima NÃO formam um triãngulo ')

