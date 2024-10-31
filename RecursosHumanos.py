
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

# Verificando a distribuição dos valores usando um boxplot
# Boxplot: Serve para mostrar algumas informações relevantes
# sobre as colunas como: a presença de outliers, o valor máximo
# de uma coluna, o valor minimo de uma coluna e a médiana dos valores
# (50%)

# Titulo do boxplot
plt.title("Boxplot da coluna de salário")

# Função que irá criar o boxplot: Ira receber como argumento a 
# coluna que será análisada.
sns.boxplot(base_dados['Salario'])

# Irá exibir o gráfico
plt.show()


# Boxplot da coluna de anos de experiencia
# Titulo do boxplot
plt.title("Boxplot dos anos de experiência")

# Criação do boxplot
sns.boxplot(base_dados['Anos de Experiencia'])

# Exibição do gráfico
plt.show()


# Agora vamos usar um scatterplot(gráfico de pontos) para análisar a
# distribuição de salários por ano.

# Scatterplot: Gráfico de pontos que mostra a relação de 2 colunas
plt.figure(figsize=(10,5))

# Titulo do gráfico
plt.title("Relação entre o salário e os anos de experiência")

# Rótulo do eixo x
plt.xlabel('Salário')

# Rótulo do eixo y
plt.ylabel('Anos de experiência')

# Função que ira cria o scatterplot: Irá receber como argumento
# a  base de dados, a coluna do eixo x e a coluna do eixo y
sns.scatterplot(data=base_dados, x='Salario', y='Anos de Experiencia')

# Irá exibir o gráfico
plt.show()


# Vamos visualizar essas informações usando um reggplot

# regplot: O regplot do Seaborn é usado para mostrar a relação entre duas variáveis e ajusta uma reta de regressão sobre os dados. Ele combina um gráfico de dispersão (scatterplot) com uma linha de tendência, que representa a melhor aproximação linear entre as variáveis.

# Titulo do gráfico
plt.title("Regplot que mostra a relação entre a coluna de salarios e a coluna de anos de experiencia usando uma reta de regressão")

# Tamanho do gráfico
plt.figure(figsize=(10,5))

# Rótulos do eixo x
plt.xlabel('Salário')

# Rótulos do eixo y
plt.ylabel('Anos de Experiência')

# Função quye ira criar o regplot: Recebe como argumento a base de dados, o valor do eixo x e o valor do eixo y
sns.regplot(data=base_dados, x='Salario', y='Anos de Experiencia')

# Ira exibir o gráfico
plt.show()


# Também é possivel verificar o nivel de correlação entre as colunas,
# onde, quanto mais próximo de 1, mais forte é a correlação entre as
# 2 colunas

print("VISUALIZANDO A CORRELAÇÃO ENTRE AS COLUNAS")

print(base_dados.corr())

# Visualizando a correlação usandi um grafico de calor

correlacao = base_dados.corr()

# O annt true possibilita que o valor da correlação apareça no gráfico
sns.heatmap(correlacao, annot=True)

plt.show()