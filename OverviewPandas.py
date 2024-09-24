

# Biblioteca do python utilizada para analise de dados com ela podemos
# realizar higienizações de dados e processos de machine learning.
# Também é possivel tratar dados com o pandas


# Import da biblioteca pandas que terá os metodos necessários
# para acessarmos o arquivo csv e tratar os dados.
import pandas as pd

# import da biblioteca np
import numpy as np

# Leitura do arquivo: é necessário atribuir a uma variável, o comando de 
# acesso ao arquivo csv para podermos acessar os metodos necessários para
# a análise de dados.
df = pd.read_csv('performanceEstudantes.csv')

# função da biblioteca pandas que ira mostrar o tipo do arquivo,
# no nosso caso é um dataframe.

# DataFrame: é uma estrutura de dados em formato de tabela que armazena
# dados em formato de linhas e colunas. É parecido com uma planilha em
# excel ou uma tabela em um banco de dados.
print("TIPO DOS DADOS")
print(type(df))

# Função da biblioteca pandas que mostra as 5 primeiras linhas de cada coluna da tabela
print("5 PRIMEIRAS LINHAS DAS COLUNAS")
print(df.head())

# Função da biblioteca pandas que mostra as 5 ultimas linhas de cada coluna da tabela
print("5 ÚLTIMAS LINHAS DAS COLUNAS")
print(df.tail())

# função da biblioteca pandas que mostra a quantidade de linhas
# e colunas da tabela
# Observação: O primeiro valor é a quantidade de linhas e o segundo
# valor é a quantidade de colunas
print("QUANTIDADE DE LINHAS E COLUNAS DA TABELA")
print(df.shape)

# Metodo da biblioteca pandas que mostra as colunas da tabela
print("COLUNAS DA TABELA")
print(df.columns)

# Verifica a quantidade de linhas duplicadas na tabela, ou seja,
# é necessário a utilização da função sum que ira somar as linhas
# duplicadas da tabela
print("QUANTIDADE DE LINHAS DUPLICADAS DA TABELA")

print(df.duplicated().sum())

# Agora se utilizarmos somente a função duplicated, ela vai nos retornar
# um valor booleano em cada linhas da tabela, onde true (verdadeiro) significa que a linha é duplicada e false (falso) representa que não há linhas duplicadas.

print("LINHAS DUPLICADAS DA TABELA")

print(df.duplicated())


# função da biblioteca pandas que contém informações gerais sobre o dataframe

print("INFORMAÇÕES GERAIS DO DATAFRAME")

print(df.info())

# Verificação da quantidade de valores nulos usando o metodo sum
print("QUANTIDADE DE VALORES NULOS")

# A função isna verifica a se há ou não valores nulos na tabela
print(df.isna().sum())


# A função isna verifica se há valores nulos na tabela e retorna
# um valor booleano em cada linha da tabela
# True: contém valores nulos
# False: não contém valores nulos.
print("VERIFICAÇÃO DE VALORES NULOS NA TABELA")

print(df.isna())

# Sumário estátistico: nos passa informações como numero de
# valores de cada coluna, a média dos valores de cada coluna, o desvio padrão de cada coluna, o valor minimo de cada coluna, os quartis de cada coluna (25% dos dados, 50% dos dados(também é a média dos valores), 70% dos dados) e o valor máximo de cada coluna.
print("DESCRIÇÃO DO SUMÁRIO ESTÁTISTICO")

# A função describe do pandas nos passa o sumário estatistico das
# colunas
print(df.describe())


# Sumário estátistico de todas as variaveis (incluindo todos os tipos
# como o de textos por exemplo)

print("SUMARIO ESTATISTICO DE TODAS AS VARIAVEIS (TODOS OS TIPOS)")

print(df.describe(include='all'))

# Ira mostrar a quantidade de valores unicos em cada coluna
print("QUANTIDADE DE VALORES ÚNICOS")
print(df.nunique())

# Com o pandas posso acessar diretamente uma determinada coluna e
# aplicar nela uma função, por exemplo, vamos verificar os valores 
# nulos da coluna 'parental level of education'.

print("QUANTIDADE DE VALORES ÚNICOS DA COLUNA 'PARENTAL LEVEL OF EDUCATION'")
print(df['parental level of education'].nunique())

# A funçaõ value_counts do pandas calcula a frequencia de valores 
# das colunas

print("FREQUENCIA DE VALORES DAS COLUNAS")

print(df.value_counts())

# Agora vamos usar o value_counts em uma coluna especifica, no caso vamos
# ver a frequência entre os generos dos alunos

print("FREQUENCIA DOS VALORES DA COLUNA GENDER")
print(df.gender.value_counts())