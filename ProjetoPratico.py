

# Projeto Unicórnio
# 'Unicornio' é um termo usado na industria de capital de risco para 
# descrever uma startup de capital fechado com valor superior a 1
# bilhão. O termo foi popularizado pela primeira vez pela capitalista
# de risco AIllen Lee, fundadora da Cowboy Ventures, um fundo de
# capital de risco com sede em Palo Alto, California.

# Unicornios também podem se referir a um fenômeno de recrutamento 
# no setor de Recursos Humanos(RH). Os gerentes de RH podem ter
# grandes expectativas para preencher um cargo, levando-os a procurar
# candidatos com qualificações superiores as exigidas para um cargo
# especifico. Em essencia, esses gerentes estão procurando um unicórnio
# o que leva a uma desconexão entre o candidato ideal e quem eles podem contratar do grupo de pessoas disponiveis. 

# Import das bibliotecas

# Ira possibilitar manipular arrays como por exemplo, realizar
# operações aritmeticas com arrays

import numpy as np

# Ira possibilitar manipular e analisar dados, além claro, de permitir
# a criação/acesso de dataframes.
import pandas as pd

# Possibilita a visualização de graficos
import matplotlib.pyplot as plt

# Possibilita a criação de vários tipos de graficos como o de dispersão,
# o de correlação,  o de linhas, etc. Também possibilita carregar datasets
# prontos que ja existem na biblioteca.
import seaborn as sns

# Biblioteca que tem como objetivo alertar ao usuário sobre 
# possiveis problemas no código
# Observação: Esses avisos não são avisos de erros, como por exemplo
# erros fatais
import warnings

# Metodo da biblioteca warning que irá ignorar todos os avisos
warnings.filterwarnings('ignore')


# O primeiro passo será acessar o dataset que será análisado.
# Iremos acessar através do metodo read_csv da biblioteca pandas

base_dados = pd.read_csv('datasetunicornio.csv')

# Agora vamos verificar a dimensão (quantidade de linhas e colunas)

print("QUANTIDADE DE LINHAS E COLUNAS DO DATASET")
# Metodo que retorna o numero de linhas e colunas do dataset
print(base_dados.shape)

# Verificação dos primeiros registros da tabela
print("PRIMEIROS REGISTROS DO DATASET")

# Irá mostrar todas as colunas do dataset, onde o none indica que o pandas
# deve remover qualquer limitação de numeros de coluna exibidas nos outputs
# do pandas. Ou seja, ao informar o None, o pandas ira entender que todas
# as colunas devem ser mostradas
pd.set_option('display.max_columns', None) 

# ira mostrar as 5 primeiras linhas de cada coluna do dataset
# Observação: é possivel passar como parametro para a função 
# head o numero de linhas que você quer visualizar
print(base_dados.head())

# Verificação das colunas existentes na tabela

print("COLUNAS DO DATASET")
print(base_dados.columns)

# Renomeando as colunas com a função rename
# Antes de iniciar o rename vamos eliminar os espaços em branco
# existentes no nome das colunas
base_dados.columns = base_dados.columns.str.strip()

base_dados.rename({
    'Company': 'Empresa'
    #'Valuation ($B)': 'Valor ($)', 
    #'Date Joined': 'Data de Adesão', 
    #'Country': 'Pais',
    #'City': 'Cidade',
    #'Industry': 'Setor',
    #'Investors': 'Investidores'
},inplace=True) # O parametro inplace=True faz com que a alteração seja aplicada diretamente no dataframe original sem a necessidade de criar
# uma cópia

# Verificando se os nomes das colunas foram modificados

print("VERIFICANDO O NOME DAS COLUNAS")

print(base_dados.columns) 