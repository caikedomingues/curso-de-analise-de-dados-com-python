

# Antes de seguir com as aulas do curso resolvi testar os meus conhecimentos

# pedindo exercicios para o chatgpt baseado no dataset que escolhi

# Dataset escolhido: IMDb Top 1000 Séries de TV

# Descrição do dataset: Este conjunto de dados contém uma lista das 1.000 séries de TV mais bem avaliadas no IMDb, classificadas pela classificação média dos usuários, com foco em títulos que receberam mais de 10.000 votos.

# import das bibliotecas necessárias

# import da biblioteca que possibilita acessar o dataset, visualizar
# os dados e manipula-los
import pandas as pd

# Import da biblioteca que possui uma grande variedade de gráficos
import seaborn as sns

# import da biblioteca que possibilita a criação, exibição e 
# manipulação de gráficos

import matplotlib.pyplot as plt

# Import que irá possibilitar manipular warnings

import warnings

# Função que irá desabilitar warnings

warnings.filterwarnings('ignore')


# Acessando o dataset análisado

base_dados_serie = pd.read_csv('series.csv')


pd.set_option("display.max_columns",None)

# Visualizando as 5 primeiras linhas

print("VERIFICANDO AS 5 PRIMEIRAS LINHAS")

print(base_dados_serie.head())

# Verificando as informaçoes gerais do dataset

print("INFORMAÇÕES GERAIS DO DATASET")

print(base_dados_serie.info())

# Antes de realizar os exercicios, vamos renomear as colunas para
# facilitar o nosso entendimento

base_dados_serie.rename(columns={
    
    'title':'Titulo',
    'genres': 'Generos',
    'averageRating': 'Avaliação Media',
    'numVotes': 'Numero de Votos',
    'releaseYear':'Ano de Lançamento'
    
}, inplace=True)

# Verificando se a alteração dos nomes funcionou

print("VERIFICANDO SE A MODIFICAÇÃO DOS NOMES FOI EXECUTADA")

print(base_dados_serie.columns)

# Verificando a quantidade de valores nulos das colunas

print("QUANTIDADE DE VALORES Nulos")

print(base_dados_serie.isnull().sum())

# Verificando a quantidade de valores únicos

print("VALORES ÚNICOS DAS COLUNAS DO DATASET")

# Para realizar a verificação, vamos percorrer a base de dados
# com o intuito de acessar cada coluna do dataframe
for coluna in base_dados_serie:
    
    # Variável que irá receber os valores únicos de cada coluna.
    # Vamos usar o metodo unique para capturar os valores únicos.
    valores_unicos = base_dados_serie[coluna].unique()
    
    # Impressão dos resultados
    print("Valores únicos da coluna {}:{}".format(coluna, valores_unicos))


# Agora, vamos verificar a quantidade de valore únicos das colunas
# do Dataset
print("TOTAL DE VALORES ÚNICOS DAS COLUNAS DO DATASET")
# Para verificar a quantidade de valores unicos, vamos
# percorrer as colunas da base de dados análisada
for coluna_serie in base_dados_serie:
    
    # Variável que irá conter a quantidade de valores unicos das colunas
    total_valores_unicos = base_dados_serie[coluna_serie].unique()
    
    # Impressão dos resultados: Como queremos descobrir a quantidade
    # de valores, precisamos usar o metodo len após a utilização da
    # função unique
    print("Total de valores únicos da coluna {}: {}".format(coluna_serie, len(total_valores_unicos)))
    


# EXERCICIOS DE ANÁLISE DE DADOS

# 1.Distribuição de Avaliações: plote um histograma da coluna averageRating. Como as avaliações estão distribuidas? Quais são
# os valores mais comuns?

# Criação do histograma usando a coluna de Avaliação Média
plt.title("Histograma da distribuição da avaliação média")

# Ira definir o tamanho da imagem do gráfico
plt.figure(figsize=(20,5))

# Criação do histograma da coluna Avaliação Media
plt.hist(base_dados_serie['Avaliação Media'])
# Exibição do gráfico
plt.show()

# Os valores mais comuns são os valores entre 8.0 e 8.8.