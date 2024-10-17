

# Sobre o conjunto de dados: Este conjunto de dados consiste nas notas obtidas pelos alunos em várias disciplinas.

# Vamos tentar entender a influência dos antecedentes dos pais, preparação
# para testes etc, no desempenho dos alunos


# Biblioteca que irá permitir análisar e manipular dados, acessar ou 
# criar dataframes

import pandas as pd

# Biblioteca que irá permitir realizar manipulações e operações com
# arrays

import numpy as np

# Biblioteca que possibilita a criação de uma variedade de gráficos

import seaborn as sns

# Biblioteca que ira permitir a criação e a visualização de gráficos
import matplotlib.pyplot as plt

# Biblioteca que é responsável por realizar avisos sobre alguns erros
# no código.
# Observação: Esses erros não são erros de sintaxes ou erros fatais,
# ele informa erros que não interrompem a execução do programa, como
# por exemplo, alguma função ou código que futuramente deixará de existir

import warnings

# Função da biblioteca warnings que ira desabilitar os avisos do warning

warnings.filterwarnings('ignore')

# Antes de iniciar qualquer processo será necessário ler/acessar 
# o dataset análisado.
base_dados = pd.read_csv('performanceEstudantes.csv')

# Verificando a dimensão do dataframe (tamanho do dataframe)

print("DIMENSÃO DO DATAFRAME")

print(base_dados.shape)

# Verificando as 5 primeiras linhas do dataframe
print("5 PRIMEIRAS LINHAS DO DATAFRAME")
# Trecho que ira permitir a visualização de todas as colunas
pd.set_option('display.max_columns', None)
# Imprimindo as 5 primeiras linhas do dataframe com o metodo head
# Observação: O método head possibilita que você passe como o parametro
# a quantidade de linhas que você quer exibir.
print(base_dados.head())

# Renomeando as colunas: Vamos usar a função rename para renomear
# as colunas de maneira que os nomes fiquem mais compreensíveis
base_dados.rename(columns={
    
    # Para funcionar, precisamos passar como parametro
    # o nome original da coluna e depois o novo nome
    # da coluna.
    'gender': 'Genero',
    
    'race/ethnicity': 'Etnia',
    
    'parental level of education': 'Nivel de educação dos pais',
    
    'lunch': 'Lanche',
    
    'test preparation course': 'Curso de preparacao',
    
    'math score': 'Nota de matemática',
    
    'reading score': 'Nota de leitura',
    
    'writing score': 'Nota de escrita'
    
}, inplace=True) # O parâmetro inplace=True modifica o DataFrame original
# sem a necessidade de criar uma cópia.

# Verificando se o nome das colunas foram alterados corretamente

print("VERIFICANDO O NOME DAS COLUNAS")
print(base_dados.columns)

# Verificando há quantidade de campos nulos em cada coluna
print("QUANTIDADE DE CAMPOS NULOS EM CADA COLUNA")
print(base_dados.isnull().sum())

# Também podemos verificar essas informações graficamente

# Atrubui a uma varoiável o comando que ira retornar valores nulos
# no dataframe
valores_nulos = base_dados.isnull()

# Ira configurar o tamanho da figura do gráfico(largura e altura)
plt.figure(figsize=(15,6))
# Titulo do gráfico
plt.title("Verificando graficamente se há nulos na tabela")

# Função da biblioteca seaborn que ira criar um grafico de calor.
# A função irá receber como parametro a base de dados analisada, que
# que ira definir a intensidade das cores e o cbar que tem como objetivo determinar se a barra de cores deve ou
# não ser exibida
sns.heatmap(valores_nulos, cbar=True)

# Exibição do gráfico
plt.show()

# Verificando a quantidade de valores unicos em cada coluna

# Os valores únicos são valores que aparecem apenas umavez na base de dados. por exemplo,se você tiver uma coluna que contém os valores [1, 2, 2, 3, 4, 4, 5], os valores únicos dessa coluna seriam [1, 2, 3, 4, 5].
# Esses dados são importantes para entendermos a diversidade de valores
# da base de dados.

print("QUANTIDADE DE VALORES ÚNICOS DAS COLUNAS")

print(base_dados.nunique())


# Verificando a descrição do dataframe
# O metodo describe tem como função retornar uma análise estatistica
# do dataframe como: 
# - a contagem de dados da coluna
# - a média dos valores
# - o desvio padrão
# - o valor mínimo
# - 25% dos dados (1º quartil)
# - 50% dos dados (mediana)
# - 75% dos dados (3º quartil)
# - o valor máximo


print("ANÁLISE ESTATISTICA DO DATAFRAME")

print(base_dados.describe())


# Verificando as informações principais do dataframe

print("INFORMAÇOES GERAIS DO DATAFRAME")

print(base_dados.info())


# Verificando a frequencia dos valores unicos da coluna Genero
# A frequencia representa a quantidade de vezes que o valor 
# aparece na base de dados.

print("FREQUENCIA DOS VALORES DA COLUNA GÊNERO")

print(base_dados['Genero'].value_counts())


# Também é possivel verificar a porcentagem da frequencia dos valores unicos
# Basta passar como parametro o normalize true, para visualizar a porcentagem.
print("FREQUÊNCIA DOS VALORES ÚNICOS DA COLUNA GÊNERO")

print(base_dados['Genero'].value_counts(normalize=True) * 100)

print("PORCENTAGEM DA FREQUENCIA DOS VALORES ÚNICOS DA COLUNA ETNIA")

print(base_dados['Etnia'].value_counts(normalize=True) * 100)


print("FREQUÊNCIA DOS VALORES ÚNICOS DA COLUNA DE NIVEL DE EDUCAÇÃO DOS PAIS")

print(base_dados['Nivel de educação dos pais'].value_counts() * 100)


print("FREQUÊNCIA DOS VALORES ÚNICOS DA COLUNA DE LANCHES")

print(base_dados['Lanche'].value_counts() * 100)


print("FREQUÊNCIA DOS VALORES ÚNICOS DA COLUNA DE DE CURSO DE PREPARAÇÃO")
print(base_dados['Curso de preparacao'].value_counts(normalize=True) * 100)


# Vamos criar um boxplot para visualizar a distribuição de notas de 
# matemática por genêro

# Metodo da biblioteca matplotlib que irá criar o titulo do gráfico
plt.title("Distribuição das notas de matematica por genero")
# Metodo da biblioteca seaborn que ira criar um gráfico boxplot,
# o metodo recebe como parametro a base de dados analisada, os
# valores que irão ocupar o eixo x e os valores que irão ocupar
# o eixo y
sns.boxplot(data=base_dados, x = 'Nota de matemática', y= 'Genero')

# Método da biblioteca matplotlib que irá mostrar
# o gráfico na tela
plt.show()


# Criação do boxplot para visualizar a distribuição das notas de leitura
# por genêro

# Irá criar o titulo do gráfico
plt.title("Distriubuição das notas de leitura por genêro")

# Método que ira criar o grafico boxplot, o método irá receber
# como parametro a base de dados analisada, os valores do eixo x 
# e os valores do eixo y. 
sns.boxplot(data=base_dados, x = 'Nota de leitura', y = 'Genero')

# Exibição do gráfico
plt.show()


# Criação do boxplot para visualizar a distribuição de notas de escrita
# por genêro

# Ira criar o titulo do gráfico
plt.title("Distribuição das notas de escrita por genêro")

# Método que irá criar o boxplot, ele irá receber como parametro
# a base de dados analisada, os valores do eixo x e os valores 
# do eixo y
sns.boxplot(data=base_dados, x = 'Nota de escrita', y = 'Genero')

# Exibição do gráfico
plt.show()


# Vamos descrever os valores da coluna de genero através de um agrupamento

print("AGRUPAMENTO POR GENERO: ANALISE DESCRITIVA DOS GENEROS NAS COLUNAS DO DATAFRAME")

# O resultado desse bloco é a analise descritiva (como contagem, média,
# desvio padrão, etc) para cada genero, aplicada a todas as colunas numéricas da base de dados.
print(base_dados.groupby(by=['Genero']).describe())


# Também é possivel fazer a mesma coisa com uma coluna especifica.

# Por exemplo, vamos visualizar a análise descritiva dos generos
# na coluna de notas de matemática.

print("ANALISE DESCRITIVA DOS GENEROS NA COLUNA DE NOTAS DE MATEMATICA")
print(base_dados.groupby(by=['Genero']).describe()['Nota de matemática'])


# Utilizando um pairplot para visualizar varios tipos de gráficos
# dos valores numéricos com o objetivo de verificar a relação entre
# diferentes variáveis numéricas
sns.pairplot(base_dados)

# exibição do gráfico
plt.show()

# também é possivel usar o pairplot em uma coluna especifica
# usando o parametro hue, que ira receber o nome da coluna
# especifica.
sns.pairplot(base_dados, hue='Etnia')

# Exibição do gráfico
plt.show()


# Vamos visualizar a distribuição das notas de matemática por genero
# usando um boxplot
sns.boxplot(data=base_dados, x = 'Genero', y = 'Nota de matemática')

# Exibição do gráfico
plt.show()


# Visualizando a distribuição das notas de matemática por nivel de educação dos pais
sns.boxplot(data=base_dados, x='Nota de matemática', y='Nivel de educação dos pais')

# Exibição do gráfico
plt.show()


# Agora vamos analisar descritivamente os valores da coluna de nível
# de educação dos pais em relação às notas de matemática. Para isso,
# vamos agrupar pela coluna de nível de educação dos pais e descrever
# os valores da coluna de notas de matemática.
# O reset index irá transformar o indice das linhas em uma coluna

print("ANALISANDO DESCRITIVAMENTE AS NOTAS DE MATEMÁTICAS DOS ALUNOS DE ACORDO COM O NIVEL DE EDUCAÇÃO DOS PAIS")
print(base_dados.groupby(by=['Nivel de educação dos pais']).describe()['Nota de matemática'].reset_index())


# Visualizando a distribuição das notas de matemática por Curso de preparação

sns.boxplot(data=base_dados, x='Nota de matemática', y='Curso de preparacao')
# exibição do gráfico
plt.show()


# Analisando descritivamente os valores da coluna de Curso de
# preparação em relação às notas de matemática. Para isso,
# vamos agrupar pela coluna de Curso de preparação e descrever
# os valores da coluna de notas de matemática.
# O reset index irá transformar o indice das linhas em uma coluna

print("ANALISANDO DESCRITIVAMENTE AS NOTAS DE MATEMÁTICA DOS ALUNOS DE ACORDO COM OS CURSOS DE PREPARAÇÃO")

print(base_dados.groupby(by=['Curso de preparacao']).describe()['Nota de matemática'].reset_index())


# O scatterplot (gráfico de dispersão) mostrará a distribuição
# ou concentração de dados numéricos correlacionados, com o objetivo
# de identificar padrões, tendências ou outliers.
sns.scatterplot(data=base_dados, x='Nota de matemática', y='Nota de escrita')

# Exibição do gráfico
plt.show()