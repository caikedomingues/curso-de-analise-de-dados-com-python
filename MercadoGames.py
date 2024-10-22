
# Conjunto de dados de vendas de videogames: Dados de vendas e classificações de jogos de videogame extaridos do VZCharts.

# Import das bibliotecas necessárias para a análise

# Biblioteca que irá acessar o dataset para possibilitar
# a manipulação e a análise dos dados
import pandas as pd

# Biblioteca que possibilita manipular arrays
import numpy as np

# Biblioteca que ira possibilitar manipular gráficos
import matplotlib.pyplot as plt

# Biblioteca que ira possibiklitar criar gráficos personalizados
# usando a classe graph_objects
import plotly.graph_objects as go

# import da biblioteca seaborn que contém uma grande variedade de gráficos

import seaborn as sns

# import da biblioteca que manipula / administra warnings

import warnings

# Função que irá desabilitar os warnings

warnings.filterwarnings('ignore')


# Acessando/lendo o dataset que será utilizado na análise
# latin-1: especifica o tipo de codificação dos caracteres
# usados para ler o arquivo csv. Essa codificação é um padrão
# para caracteres acentuados, usados em linguas como o portugues
# espanhol, frânces, entre outras.
# Nesse caso específico, a leitura pode não funcionar corretamente sem  essa codificação, pois caracteres especiais podem ser exibidos de forma incorreta.
base_dados = pd.read_csv('Games.csv', encoding='latin-1')


# Metodo que irá possibilitar que todas as colunas sejam mostradas
pd.set_option("display.max_columns", None)

# Ira mostrar as 5 primeiras linhas
print("VISUALIZANDO AS 5 PRIMEIRAS LINHAS DA BASE DE DADOS")
print(base_dados.head())


# Analisando a dimensão (tamanho) da base de dados, a função irá
# retornar 2 valores: o numero de linhas e o numero de colunas.
print("DIMENSÃO DA BASE DE DADOS")

print(base_dados.shape)


# Renomeando as colunas do dataset

base_dados.rename(columns={
    
    
        'Game':'Jogo',
        'Year': 'Ano',
        'Genre': 'Genero',
        'Publisher':'Editora',
        'North America': 'America do Norte',
        'Europe': 'Europa',
        'Japan':'Japao',
        'Rest of World':'Resto do mundo'
}, inplace=True)

# Verificando se os nomes foram alterados

print("Verificando a renomeação das colunas")

print(base_dados.columns)

# Verificando a quantidade de valores nulos na tabela

print("QUANTIDADE DE VALORES NULOS")

print(base_dados.isnull().sum())

# Verificando os valores nulos de forma gráfica usando o heatmap (mapa
# de calor).

# Ira configurar o tamanho do gráfico
plt.figure(figsize=(14,6))

# Ira criar o titulo do gráfico
plt.title("Verificando os valores nulos de forma gráfica")

# Ira criar o grafico de calor: A função ira receber como parametro
# a função isnull do pandas
sns.heatmap(base_dados.isnull())

# Exibição do grafico
plt.show()

# Após a verificação dos valores, vamos apagar os valores nulos
# da tabela usando a função dropna(), que ira receber como parametro
# as colunas que terão suas linhas nulas excluidas.
# É necessário passar o parametro inplace = True para garantir
# que a modificação seja feita no dataset original.
base_dados.dropna(subset=['Ano'], inplace=True)

base_dados.dropna(subset=['Editora'], inplace=True)

print("VERIFICANDO SE OS VALORES NULOS FORAM APAGADOS")

print(base_dados.isnull().sum())

print("VERIFICANDO A DIMENSÃO DA BASE DE DADOS APÓS A EXCLUSÃO DE VALORES NULOS ")

print(base_dados.shape)

# Descrição analitica da base de dados

print("DESCRIÇÃO ANÁLITICA DA BASE DE DADOS")

print(base_dados.describe())

# Vamos criar um gráfico de barras usando a biblioteca seaborn.
# A função barplot que cria os gráficos irá receber como parametro
# a base de dados, os valores do eixo x e os valores do eixo y.

#ira criar o titulo do gráfico que ficara alinhado a esquerda e 
# terá tamanho 14
plt.title("Quantidade de vendas globais(mi)", loc= 'left', fontsize=14)

plt.figure(figsize=(10,5))

# Rótulo do eixo Y
plt.ylabel("Quantidade de vendas")

# Irá criar o gráfico de barras
# c1 = None: Desabilita a exibição dos intervalos de confiança. Apenas as barras são exibidas, sem linhas de erro.
# Color: ira definir a cor das barras do gráfico.
# Estimator: No Seaborn, o parâmetro estimator no método barplot permite que você defina qual função será aplicada aos dados numéricos para gerar os valores representados pelas barras.
# Por padrão, o barplot usa a média (mean) dos valores como estimador. No entanto, você pode usar qualquer outra função agregadora, como a soma (sum), contagem (len), mediana (median), etc.
sns.barplot(data=base_dados, x = 'Ano', y='Global', ci=None, color='#69b3a2', estimator=sum)

# Exibição do gráfico
plt.show()

# Como os anos 2019 e 2020 não tiveram vendas, vamos retirar eles da coluna de anos. Para isso, vamos usar o comando loc para filtrar
# os anos (2019, 2020) com o intuito de não mostrar mais eles na 
# base de dados

# Basicamente, vamos passar como condição do loc, todos os valores 
# diferentes de 2019 e 2020 com o objetivo de remover esses anos 
# da base de dados
base_dados = base_dados.loc[(base_dados['Ano'] != '2019') & (base_dados['Ano'] != '2020')]

print("VERIFICANDO SE OS ANOS 2019 E 2020 FORAM OCULTADOS")

print(base_dados.head())


# Agora vamos analisar a distribuição dos dados da coluna 'Global'
# usando um grafico kdeplot da biblioteca seaborn
# kdeplot: Serve para visualizar a de uma variável continua, mas 
# em vez de mostrar barras, ele desenha uma linha que representa
# a densidade de probabilidade dos dados.

# Ira configurar o tamanho da imagem do gráfico
plt.figure(figsize=(12,5))

# irá definir o titulo do gráfico alinhado a esquerda com tamanho 14

plt.title('Distribuição das vendas globais', loc='left', fontsize=14)

# Ira adicionar grades no fundo gráfico
plt.style.use('ggplot')

# função que irá construir o kdeplot da coluna 'Global'
# shade: Este argumento preenche a área abaixo da curva
# de densidade com uma cor.
# bw: irá definir a largura da banda(suavização da curva de densidade no gráfico.) o que pode afetar as variações dos dados
# color: Define a cor da curva
# linewidth: define a largura da linha.
sns.kdeplot(base_dados['Global'], shade=True, bw=1, color='#96a8a8', linewidth=2.5)

# Irá definir o rótulo do eixo y
plt.ylabel('Densidade')

# Irá exibir o gráfico
plt.show()


# Verificando o total de vendas por ano: Para realizar essa ação,
# vamos agrupar os dados por ano e calcular o total de valores em
# cada coluna.

print("VENDAS POR ANO")

print(base_dados.groupby(by=['Ano']).sum())


# Visualiando a distribuição global por ano usando o boxplot da 
# biblioteca seaborn

# Irá definir o tamanho do gráfico
plt.figure(figsize=(10,5))

# Irá definir o titulo do gráfico
plt.title("Distribuição das vendas globais por ano")

# Rótulo do eixo x
plt.xlabel("Vendas globais")

# Função que irá criar o boxplot, ela ira receber como a parametro
# a base de dados com os valores, os valores do eixo x(ano) e os
# valores do eixo y(Vendas globais).
sns.boxplot(data=base_dados, x = 'Ano', y = 'Global')

# Exibição do gráfico
plt.show()

# Vamos usar a função loc para visualizar valores maiores ou iguais
# a 10 (milhões) da coluna 'global'

print("VISUALIZANDO VALORES MAIORES OU IGUAIS A 10 NA COLUNA DE VENDAS GLOBAIS")

# Função que irá filtrar os valores maiores ou iguais a 10
print(base_dados.loc[(base_dados['Global'] >= 10)])





