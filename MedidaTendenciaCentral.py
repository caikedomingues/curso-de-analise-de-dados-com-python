

# Estatistica Descritiva: Em sua essência, a estatistica é a ciência que
# apresenta porcessos próprios para coletar e interpretar adequadamente
# conjunto de dados, sejam eles numéricos ou não. Pode se dizer que seu
# objetivo é o de apresentar informações sobre os dados em análise
# para que se tenha maior compreensão dos fatos que os mesmos representam
# A estatistica descritiva, como o próprio nome diz, se preocupa em descrever os dados


# Módulo 1: Medidas de tendencia central
# São chamadas assim porque indicam um ponto em torno do qual se
# concentram os dados.

# Para manipular dados
import pandas as pd

# Para criar graficos gráficos
import seaborn as sns

# visualizar dados 
import matplotlib.pyplot as plt

# Os warnings são mensagens que o python emite para alertar os programadores sobre condições que podem indicar um problema, mas que não
# são erros fatais. Ao contrário de um erro, que interrompe a execução
# do programa, um warning é uma notificação qe informa que algo pode estar
# errado ou que você deve estar ciente de uma situação especifica.
# Ele não interrompe a execução de um programa
import warnings

# Tem como objetivo manipular as mensagens de warning, no nosso caso,
# vamos ignorar todas as mensagens
warnings.filterwarnings('ignore')


# Função do seaborn que ja possui alguns datasets prontos, no nosso caso
# vamos carregar o dataset 'iris'

base_dados = sns.load_dataset('iris')


# 5 primeiras linhas do dataset iris

print("5 PRIMEIRAS LINHAS DO DATASET")

print(base_dados.head())


# O metodo shape conta a quantidade de linhas e colunas do dataset

print("QUANTIDADE DE LINHAS E COLUNAS")

print(base_dados.shape)

# Média aritmética: a média aritemética é a soma de todos os valores
# observados da variável dividida pelo número total deobservações

# No nosso caso vamos tirar a média aritemética dos valores da coluna 
# 'petal_length' (tamanho das petalas)

print("MÉDIA DOS TAMANHOS DAS PETALAS")
print(base_dados['petal_length'].mean())

# moda: é o valor que apresenta a maior frequencia de variável entre os valores observados 

print("MODA DOS VALORES APRESENTADOS")
print(base_dados['petal_length'].mode())


# Mediana: E o valor que ocupa a posição central da série de observações
# de uma variável, em rol, dividindo o conjunto em 2 partes iguais, ou seja,
# a quantidade de valores inferiores a mediana é igual á quantidade de valores superiores a mesma.

print("MEDIANA DO TAMANHO DAS PETALAS")
print(base_dados['petal_length'].median())

