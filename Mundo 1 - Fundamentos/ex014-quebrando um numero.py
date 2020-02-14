
from math import trunc  # modulo usado para mostrar um numero interio de um valor decimal
n = float(input('\nDigite um número: '))
print('O número {} tem a sua porção inteira {}'.format(
    n, trunc(n)))  # comando para mostrar o numero inteiro
