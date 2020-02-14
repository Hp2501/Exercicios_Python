# Programa para selecionar aleatótiamente

from random import choice  # modulo para escolher aleatoriamente um item de uma lista
n1 = str(input('\nPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]  # comando para formar uma lista
escolhido = choice(lista)  # comando para fazer o sorteio
print('\nO aluno escolhido foi {}'.format(escolhido))
