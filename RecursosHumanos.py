
# Neste projeto vamos estudar sobre: Tempo de Experiência vs Salário 

# Import das bibliotecas necessárias

# Import da biblioteca que ira possibilitar acessar o dataset,
# manipular os dados, analisar os dados, etc
import pandas as pd

# Import da biblioteca que ira possibilitar criar e manipular
# gráficos

import matplotlib.pyplot as plt

# Import da bibilioteca que contém uma grande variedade de 
# gráficos

import seaborn as sns

# Import da biblioteca que administra warnings

import warnings

# Função que irá desabilitar warnings

warnings.filterwarnings('ignore')


# Acessando o dataset

base_dados = pd.read_csv('salarios.csv')


# Visualizando as 5 primeiras linhas

print("5 PRIMEIRAS LINHAS DO DATASET")

print(base_dados.head())

# informações gerais do dataset

print("INFORMAÇÕES GERAIS DO DATASET")

print(base_dados.info())

# Função que irá garantir que todas as linhas do dataset apareçam

pd.set_option('display.max_rows', None)

# Renomeando as colunas da base de dados. O inplace True ira garantir
# que a alteração seja aplicada na base de dados original

base_dados.rename(columns={
    
    'YearsExperience': 'Anos de Experiencia',
    'Salary': 'Salario'
}, inplace=True)

# Verificando se a alteração dos nomes funcionou

print("VERIFICANDO OS NOMES DAS COLUNAS (APÓS A RENOMEAÇÃO)")

print(base_dados.columns)

# Verificando o tamanho da base de dados

print("TAMANHO DA BASE DE DADOS")

print(base_dados.shape)


# Verificando o total de nulos (só para exercitar, pois, já vimos que não
# existem valores nulos no info)

print("TOTAL DE VALORES NULOS")

print(base_dados.isnull().sum())

# Descrição análitica do dataframe

print("DESCRIÇÃO ANÁLITICA DA BASE DE DADOS")

print(base_dados.describe())


# vamos criar um kdeplot para análisar os valores do salário

# kdeplot: Gráfico de linhas que mostra a distribuição e concentração 
# dos dados (densidade) usando uma curva suavea

# Titulo do gráfico
plt.title("Análisando a densidade da coluna de salário")

# Rótulo do eixi y
plt.ylabel("Densidade")

# Função que ira criar o grafico kdeplot, a função recebe como parametro
# a coluna que será análisada e a cor da curva (verde)
sns.kdeplot(base_dados['Salario'], color='green')

# Ira exibir o gráfico.
plt.show()