

# Numpy: Fornece um grande conjunto de de funções e operações de biblioteca que ajudam os programadores a executar facilmente
# cálculos numéricos. Mas em Numpy, as dimensões são chamadas
# de eixos. O número de eixos é classificado. Em termos mais 
# simples, quando você tem mais de uma matriz unidimensional,
# então o conceito de eixo surge. Por exemplo, a matriz 2D
# tem 2 eixos.


# import da biblioteca

import numpy as np


# É possivel verificar se a versão da biblioteca
print("Versão da biblioteca numpy: ",np.__version__)

# Para criar uma matriz, basta usar o metodo array da biblioteca
# numpy. O array ira receber como parâmetro os valores que irão
# compor o array.

array_numpy = np.array([10, 20, 30, 40, 50])
print("VALORES DO ARRAY: ", array_numpy)

# Verificação do tipo dos dados, ele irá retornar o tipo como
# um "numpy.ndarray". 
# ndarray: Significa que o array pode conter qualquer tipo de dado, onde
# o nd simboliza que o array pode ter qualquer dimensão (1D, 2D, 3D, etc)
print("TIPO DOS DADOS: ", type(array_numpy))


# Como vimos anteriormente, a função array da biblioteca numpy
# suporta inumeras dimensões (múltiplos arrays, onde cada array 
# representa uma dimensão)
# Array de 2 dimensões
dias = np.array([
    
    [10, 9, 8, 7, 6],
    
    [5, 4, 3, 2, 1]
] 
)


print("Array de 2 dimensões: ", dias)


# Array de tres dimensões

tres_dimensoes = np.array([
    
    [15, 14, 13, 12, 11],
    
    [10, 9, 8, 7, 6],
    
    [5, 4, 3, 2, 1]
])

print("Array de 3 dimensões: ", tres_dimensoes)

# Também é possivel gerar arrays de valores numéricos de maneira mais
# rápida, caso os valores sejam sequencias, para isso, basta, usar o
# método arange que ira receber como parâmetro o valor da sequencia
# numérica.
print("Array com valores de 0 a 9: ", np.arange(10)) 

# É possivel verificar o tamanho de um array

# Vamos gerar um array sequencial de 0 a 999 usando o arange
# depois iremos verificar o seu tamanho

array_1000 = np.arange(1000)

print("Valores do array 1000: ", array_1000)

print("Tamanho do array: ", len(array_1000))

