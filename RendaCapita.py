# Conjunto de dados Econômicos do Brasil 

# Dados da renda per capita dos estados união

# Renda per Capita: É um dos indicadores socioeconomicos que avaliam
# o grau de desenvolvimento econômico de um determinado lugar. A
# média é obtida através da divisão do Produto Nacional Bruto


# Import das bibliotecas necessárias para a análise

# Import da biblioteca que irá possibilitar acessar, manipular
# e modificar os dados do dataset
import pandas as pd

# biblioteca que possui uma grande quantidade de gráficos

import seaborn as sns

# Biblioteca que ira possibilitar criar e personalizar gráficos
import matplotlib.pyplot as plt


# Acessando os dados do dataset
base_dados = pd.read_csv('dadospib.csv')

# Mostrando as 5 primeiras linhas do dataframe

print("AS 5 PRIMEIRAS LINHAS DO DARAFRAME")

print(base_dados.head())

# Visualizando as informações gerais do dataframe
print("INFORMAÇÕES GERAIS DO DATAFRAME")

print(base_dados.info())

# para facilitar a nossa análise, vou renomear a coluna 'Territorialidades' para 'Territórios'

base_dados.rename(columns={
    
    'Territorialidades': 'Territorio'
    
}, inplace=True)

# Visualizando a se o nome da coluna foi alterado

print("VERIFICANDO SE O NOME DA COLUNA FOI ALTERADO")

print(base_dados.columns)

# Verificando o total de valores nulos das colunas

print("TOTAL DE VALORES NULOS DAS COLUNAS")

print(base_dados.isnull().sum())

# Convertendo para numérico possiveis valores objects da coluna 
# 'PIB per capita'.

# Antes das conversões, precisamos substituir as virgulas por pontos
# usando o metodo replace que recebe como argumento o valor que será
# substituido  e valor que irá substituir o valor anterior
base_dados['PIB per capita'] = base_dados['PIB per capita'].str.replace(',', '.')


# Trecho que ira transformar os valores da coluna 'PIB per capita'
# em tipos numéricos.

base_dados['PIB per capita'] = pd.to_numeric(base_dados['PIB per capita'])

# Também será interessante converter a coluna de 'Ano' para Date
# O format (argumento opcional) serve para configurar o formato que a data será representada
# na coluna
base_dados['Ano'] = pd.to_datetime(base_dados['Ano'], format='%Y')

# Após a conversão, vamos extrair apenas o ano da data
base_dados['Ano'] = base_dados['Ano'].dt.year

# Verificando se as conversões funcionaram
print("VERIFICANDO SE AS CONVERSÕES FUNCIONARAM")

# Ira retornar o tipo das colunas
print(base_dados.dtypes)

# verificando se os pontos foram adicionados no valor da coluna
# de PIB

print("VERIFICANDO SE AS VIRGULAS FORAM SUBSTITUIDAS")
print(base_dados.head())


# Agrupando os dados por território
print('AGRUPANDO OS DADOS POR TERRITÓRIO')

# Trecho que ira permitir que todas as linhas sejam mostradas no dataframe
pd.set_option('display.max_rows', None)

# Vamos agrupar os valores por território para ver a média dos
# territórios nas colunas numéricas do dataframe
print(base_dados.groupby(by=['Territorio']).mean())


# Agrupando os dados por território e ano

print("AGRUPANDO OS DADOS POR TERRITÓRIO E ANO")

# Nesse trecho ele vai retornar a média dos valores da coluna
# 'Território' em cada coluna nummerica por ano.
print(base_dados.groupby(by=['Territorio', 'Ano']).mean())

# A idéia principal é criar um relatório utilizando o seaborn
# para criar um grid de graficos (até onde entendi é uma imagem
# que contem varios tipos de graficos diferentes)

# Primeiro, vamos definir a cor de fundo da imagem dos gráficos
cor_fundo = '#f5f5f5'

# Para funcionar melhor esse exercicio vamos pegar apenas 7 linhas do 
# do dataframe

# Criando o sistema de grids
# FacetGrid: é uma estrutura de gráficos do seaborn que permite criar 
# uma grade de subgráficos, onde cada subgráfico representa um subconjunto dos dados com base em alguma caracteristica(variável).

# base_dados: DataFrame que contem os dados que serão utilizados na 
# construção dos graficos

# col: é usada para dividir os dados em colunas, criando um gráfico
# separado para cada valor único da variável ('território' no caso).
# Ou seja, ele vai criar uma faceta (um subgráfico) para cada território 
# presente no Dataframe 'base_dados'.

# hue: Define uma variável para a qual as cores dos gráficos serão atribuidas. Nesse caso, como é a mesma variável Territorio, o seaborn
# usará cores diferentes para representar os diferentes territórios 
# dentro de cada faceta.

# col_wrap: Define quantas colunas de subgraficos serão exibidas antes
# de ir para a proxima linha. Nesse caso, col_wrap=4 significa que serão
# exibidos até 4 subgraficos por linha. Se houver mais de 4 territórios
# unicos, as facetas seguintes irão para a linha seguinte.
grid_graficos = sns.FacetGrid(base_dados, col='Territorio', hue='Territorio', col_wrap=4, height=40)


# Comando que irá adicionar um gráfico de linhas em cada gráfico. Infelizmente, acho que como estou fazendo pelo vscode, não irei 
# conseguir deixar o grafico muito organizado por conta da quantidade
# de dados da base. Ja tentei reduzir a quantidade de linhas, porém,
# alguns graficos ficam sem linhas por conta da falta de dados para
# construção das linhas.
grid_graficos = grid_graficos.map(plt.plot, 'Ano', 'PIB per capita')

plt.show()

