print('{:-^40}'.format(' AMANDA SANDÁLIAS '))
preco = float(input('Preço das compras: R$'))
print('''Formas de pagamento:
[1] avista em espécie (ganha -10%)
[2] avista no cartão (ganha -5%)
[3] em até 2x no cartão (sem juros)
[4] em até 3x ou mais no cartão (acréscimo de 20%)''')
opcao = int(input('\nDigite a opção desejada: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('O valor da compra de R${:.2f} com 10% de desconto custará R${:.2f} '.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('O valor da compra de R${:.2f} com 5% de desconto custará R${:.2f}'.format(preco, total))
elif opcao == 3:
    total = preco / 2
    print('O valor da compra de R${:.2f} será parcelado em 2x de R${:.2f} SEM JUROS'.format(preco, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    nump = int(input('Número de parcelas: '))
    parc = total / nump
    print('o valor da compra de R${:.2f} COM JUROS DE 20% irá para R${:.2f} '
          'e será parcelado em {}x de R${:.2f}'.format(preco, total, nump, parc))
else:
   print('Opção invalida. Tente novamente! ')
