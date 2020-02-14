# Progra de Testes do "is"

a = input('\nDigite algo: ')
print('\nO tipo primitivo desse valor é {}'.format(type(a)))#verificar o tipo primitivo de um valor
print('\nSo tem espaços? {}'.format(a.isspace()))#verificar se um valor so tem espaços
print('É um número? {}'.format(a.isnumeric()))  # verificar se um valor é númerico
print('É alfabético? {}'.format(a.isalpha()))#verificar se um valor é  alfabetico
print('É alfanumérico? {}'.format(a.isalnum()))#verificar se um valor é alfanúmerico
print('Está em maiúscula? {}'.format(a.isupper()))#verificar se um valor esta em maiúsculo
print('Está em minúscula? {}'.format(a.islower()))#verificar se um valoor está em minúsculo
print('Está capitalizada? {}'.format(a.istitle()))#verificar se um valor está capitalizado
