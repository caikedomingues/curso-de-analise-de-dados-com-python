

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

# Assim como as listas, é necessário saber acessar os itens de um array numpy

print('Acessando a 1° dimensão do array dias: ', dias[0])

print("Acessando a 1° posição da 1° dimensão: ", dias[0][0])


print("Ultima dimensão do array dias: ", dias[-1])

print("Ultima posição do 1° array: ", dias[-1][-1])

# É possivel somar, subtrair, dividir ou multiplicar os valores de um array, por exemplo, vamos somar a primeira posição da primeira dimensão com a 1° posição da ultima dimensão do array dias
# Como vimos anteriormente, para acessarmos os elementos do array
# 2d temos que acessar a dimensão(linha) do array e a posição do valor que
# queremos acessar.
soma_arrays = dias[0][0] + dias[1][4]

print("Soma dos arrays: ", soma_arrays)


# Também é possivel realizar operações lógicas usando arrays

print("São iguais? ", dias[0][0] == dias[1][4])

print("São diferentes? ", dias[0][0] != dias[1][4])


# Acessando o tamanho do array de dimensões
# 1° valor: O tamanho da linha (dimensões)
# 2° valor: A quantidade de colunas
print("Tamanho do array de dimensões: ", dias.shape)

# É possivel percorrer o array usando o loop

for loop in dias:
    
    print("Valores do array dias: ", loop)
    
    
# Percorrendo apenas uma dimensão do array multidimensional

for loop in dias[0]:
    
    print("Primeira dimensão do array dias: ", loop)

# É possivel converter um array em um dataframe usando o pandas

import pandas as pd

data_frame_array = pd.DataFrame(dias)

print("CONVERTENDO ARRAY EM UM DATAFRAME")

print(data_frame_array)

# Podemos alterar o nome das colunas do dataframe gerado por um array

print("ALTERANDO O NOME DA COLUNA")

# Para alterar basta usar o parametro columns que ira receber como
# valor, uma lista de nomes para cada coluna
# Observação: se você não nomear todas as colunas a função dataframe 
# ira apresentar erro.
alterando_a_coluna = pd.DataFrame(dias, columns=['Coluna1', 'Coluna2', 'Coluna3', 'Coluna4', 'Coluna5'])

print(alterando_a_coluna)