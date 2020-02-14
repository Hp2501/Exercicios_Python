#Programa para calcular Desconto

pn = float(input('\nPreço normal do produto: R$'))
nv = pn - (pn * 5 / 100)
print('O preço normal do produto é {:.2f}!\nhoje esta com um desconto de 5%, esta saindo por R${:.2f}!'.format(pn, nv))

