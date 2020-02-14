# Programa para colocar em ordem aleatória uma lista

# modulo para escolher aleatoriamente todos os intes de uma lista
from random import shuffle
n1 = str(input('\nPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]  # comando para montar uma lista
shuffle(lista)  # comando para sortear a lista
print('\nA ordem de apresentação será ')
print(lista)
