

# import das bibliotecas
import pandas as pd

# Biblioteca que é fornece suporte para arrays multidimensionais
# e uma vasta coleção de funções matemáticas para operações com
# arrays
import numpy as np

# é uma sub-blioteca do matplotlib, que é uma biblioteca para criação
# e visualização de dados. O pyplot possibilita que você crie figuras
# e depois adicione elementos a ela, como eixos, linhas, rótulos, etc.
import matplotlib.pyplot as plt

# A função serve para inicializar o gerador de numeros aleatórios
# com uma semente especifica (no caso o 7) que garante que a sequencia
# de numeros aleatórios seja a mesma toda vez que o código for executado
np.random.seed(7)

# vetor com os numeros inteiros aleatórios entre 1 e 1.500 com 10
# amostras(gera um array de numeros inteiros aleatórios)
# low: menor valor que pode ser gerado
# high: o maior valor que pode ser gerado (no caso 1499, já que a contagem começa no 0)
# size: numeros de amostras que serão geradas
y = np.random.randint(low = 1, high = 1500, size = 10)

# Impressão do gráfico de linhas
print("VALORES GERADOS: ", y)

print("GRÁFICOS DE LINHAS")
plt.plot(y)

plt.show()

# Vamos aprimorar o grafico anterior e torna-lo mais intuitivo e apresentável

# Criando a primeira linha

# y: é o vetor de valores que você quer plotar no eixo Y

# color: Define a cor da linha usando códigos hexadecimais

# marker: Define o tipo de marcador que irão destacar os
# de dados individuais no gráfico

# ms: Tamanho dos marcadores (ms significa 'marker size')

# mec: Define  cor dos contornos dos marcadores como preto ('k')

# markerfacecolor: Define a cor do preenchimento do marcador como branco('w)

# ls: estilo da linha onde -. represe ta uma linha tracejada e pontilhada

plt.plot(y, color='#749187', marker = 'o', ms = 5, mec = 'k', markerfacecolor='w', ls = '-.')


# Criando a segunda linha

# Esse trecho adiciona uma segunda série de dados ao gráfico
# y*2: Os valores do vetor y são multiplicados por 2, criando
# uma nova linha com valores dobrados
# marker: define o simbolo do marcador
# color: define a cor da linha
# ms: tamanho dos marcadores
plt.plot(y*2, marker='+', color = 'k', ms = 5)

# rótulos
# plt.xlabel('EIXO X'): define o nome do eixo x
# plt.ylabel('EIXO Y'): define o nome do eixo y
# color: define a cor do eixo
# size: define o tamanho da fonte do rótulo
# title: define o titulo do gráfico
# loc: define o alinhamento do texto como: left, right ou center

plt.xlabel('EIXO X', color = 'red', size=12)
plt.ylabel('EIXO Y')
plt.title('TITULO', loc = 'left')

# gridlines(linhas de grade)
# axis: linhas de grades, recebe como valor o eixo que irá receber
# as linhas de grades.
# color: define a cor da linha de grade
# linestyle: define o estilo da linha de grade
# linewidth: define a espessura da linha de grade
# alpha: define a transparencia das linhas de grades (um valor entre 0 e 1)
plt.grid(axis='y', color='gray', linestyle='--', linewidth = 1, alpha = 0.8)

# Exibição do gráfico
plt.show()


np.random.seed(6)

x = np.arange(1, 11)

y1 = np.random.randint(1, 400, 10)

y2 = np.random.randint(150, 500, 10)

y3 = np.random.randint(200, 600, 10)

