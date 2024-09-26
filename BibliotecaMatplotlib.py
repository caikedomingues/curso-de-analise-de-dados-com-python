

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

# criação de 3 graficos que ficarão na mesma tela/espaço

# inicialização do gerador de números aleatórios com a semente 6
# para garantir que os valores gerados sejam sempre os mesmos
np.random.seed(6)

# Criação de um array numeros inteiros de 1 a 10
x = np.arange(1, 11)

# irá gerar 10 numeros inteiros aleatórios entre 1 e 399
y1 = np.random.randint(1, 400, 10)

# Ira gerar 10 numeros aleatórios de 150 a 499
y2 = np.random.randint(150, 500, 10)

# Ira gerar 10 numeros de 200 a 599
y3 = np.random.randint(200, 600, 10)

# Os valores de y1, y2, e y3 são usados como os valores no eixo Y 
# para os gráficos de linha que serão criados


# Define o tamanho da figura onde o 1° valor é a largura e o 2° valor
# é a altura da imagem / grafico
plt.figure(figsize=(15,5))

# Define o titulo principal da figura e o tamanho da fonte.
plt.suptitle('Figura', fontsize=15)

# Cria o primeiro subplot em uma grade de 1 linha e 3 colunas, na
# primeira posição
plt.subplot(1, 3, 1)

# Plota os valores de y1 contra x com a cor preta(k para black)
plt.plot(x, y1, color='k')

# Define o titulo do subplot e adiciona um espaçamento extra de 
# 10 unidades entre o titulo e o gráfico
plt.title('subplot 1', pad = 10)

# Define os rótulos / titulos dos eixos x e y
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')


# cria o segundo subplot na segunda posição da grade
plt.subplot(1, 3, 2)

# plota os valores y2 contra x com a cor vermelho (r para red)
plt.plot(x, y2, color='r')

# define o titulo do subplot  e adiciona um espaçamento extra
# de 10 unidades
plt.title('subplot 2', pad=10)

# Titulo dos eixos x e y
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')

# Cria o terceiro subplot na terceira posição da grade
plt.subplot(1, 3, 3)

# plota os valores y3 contra x com cor verde (g para green)
plt.plot(x, y3, color='g')

# Titulo do subplot com espaçamento de 10 unidades
plt.title('subplot 3', pad=10)

# titulo / rótulo dos eixos x e y
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')

# Ajusta o layout da figura, garantindo que os subplots não se 
# sobreponham. A figura tera um espaçamento de 4 unidades entre
# os subplots
plt.tight_layout(pad=4)

# exibição da figura
plt.show()


# Outra forma de gerar vários graficos em um mesmo espaço/imagem

# fig: objeto da figura principal que agrupa os subplots
# ax: Uma matriz(lista) de objetos axes, que são eixos
# individuais de cada subplot
# figsize: define o tamanho da imagem (largura e altura)
fig, ax = plt.subplots(1, 3, figsize = (15,5))

# Define o titulo da principal da figura, que é exibido no topo
# da figura
fig.suptitle('Figure')

# plot dos valores y1 contra o x  no primeiro subplot de cor preta
ax[0].plot(x,y1, color='black')

# plot dos valores y2 contra o x no segundo subplot de cor
# vermelha
ax[1].plot(x, y2, color='red')

# plot dos valores y3 contra x no terceiro subplot da cor verde
ax[2].plot(x, y3, color='green')

# for que ira percorrer os subplots de 0 a 2
for i in range(3):
    
    # dentro do loop vamos usar o metodo set para ajustar:
    
    # o titulo: title (f'subplot {i+1}) define o titulo de cada subplot 
    # define o rotulo do eixo x
    # define o rótulo do eixo y
    ax[i].set(title=f'subplot {i+1}', xlabel = 'EIXO X', ylabel='EIXO Y')

# Exibição dos gráficos
plt.show()