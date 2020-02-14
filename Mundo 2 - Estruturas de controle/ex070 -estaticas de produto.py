total = 0
maiord_mil = 0
menor_p = {}
p_maior_mil = ''
lista_produto = []

while True:
    print('-' * 35)
    print('\tLOJA SUPER BARATÃO')
    print('-' * 35)

    n_produto = str(input('Nome do Produto: ')).strip().upper()
    p_produto = float(input('Preço: R$ '))
    menor_p.update({n_produto: p_produto})
    lista_produto.append(n_produto)
    total += p_produto
    
    if p_produto > 1000:
        maiord_mil += 1
        p_maior_mil += n_produto
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        print('\n{:-^35}'.format('FIM DO PROGRAMA'))
        break

retorna_menor = min(menor_p.items(), key=lambda p: p[1])
print(f'\nO total da compra foi R${total:.2f}. Produtos -> ({lista_produto})')
print(f'Temos {maiord_mil} produto(s) custando mais de R$1000.00, que foi o ({p_maior_mil})')
print(f'O produto mais barato foi ({retorna_menor[0]}) e seu valor foi R${retorna_menor[1]:.2f}')
