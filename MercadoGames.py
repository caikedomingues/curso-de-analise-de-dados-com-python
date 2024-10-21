
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

