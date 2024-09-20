
# Pacote Random

# Este módulo implementa geradores de números aleatórios para 
# várias distribuições

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8]

# Com o random é possivel retornar um valor aleatório de uma lista,
# por exemplo, vamos retorna um valor aleatório da lista criada
# ácima

# Com a função choice, podemos pegar aleatoriamente um valor 
# da lista criada para esse exercicio
print("Valor aleatório da lista: ",random.choice(lista))

# Também é possivel sortear palavras

lista_nomes = ['Caike', 'Caio', 'Fernando']

print("Nome aleatório: ", random.choice(lista_nomes))

# A função random gera valores aleatórios entre 0 e 1

print("Valores aleatórios entre 0 e 1: ", random.random())

# é possivel determinar um intervalo de numeros que serão gerados

print("Intervalo de 0 a 10: ", random.randint(0,10))