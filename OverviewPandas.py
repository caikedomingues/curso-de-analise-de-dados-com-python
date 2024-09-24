

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


print("TIPO DOS DADOS")

# função da biblioteca pandas que ira mostrar o tipo do arquivo,
# no nosso caso é um dataframe.
print(type(df))


print("5 PRIMEIRAS LINHAS DAS COLUNAS")

# Função da biblioteca pandas que mostra as 5 primeiras linhas de cada coluna da tabela

print(df.head())


print("5 ÚLTIMAS LINHAS DAS COLUNAS")
# Função da biblioteca pandas que mostra as 5 ultimas linhas de cada coluna da tabela
print(df.tail())


print("QUANTIDADE DE LINHAS E COLUNAS DA TABELA")
# função da biblioteca pandas que mostra a quantidade de linhas
# e colunas da tabela
# Observação: O primeiro valor é a quantidade de linhas e o segundo
# valor é a quantidade de colunas
print(df.shape)

print("COLUNAS DA TABELA")

# Metodo da biblioteca pandas que mostra as colunas da tabela

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