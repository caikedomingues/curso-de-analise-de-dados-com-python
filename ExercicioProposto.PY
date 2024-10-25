

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

# 2.descobrir a série mais antiga, qual é a série mais antiga do dataset
# e em que ano foi lançada

# Primeiro vou tentar ordenar os anos em ordem crescente (do menor para o maior)
anos_em_ordem_crescente = sorted(base_dados_serie['Ano de Lançamento'].unique())
print("Valores únicos da coluna Ano de Lançamento em ordem crescente: ", anos_em_ordem_crescente)

# Vou tentar filtrar os titulos que tenham o ano igual a 1951
# Essa variável que ira conter o filtro das séries lançadas em 1951 (mais antigo)
# Vamos filtrar as séries usando a função loc que irá conter a condição para o 
# filtro.
titulos_lancados_em_1951 = base_dados_serie.loc[base_dados_serie['Ano de Lançamento'] == 1951]

# Ira definir o tamanho do gráfico
plt.figure(figsize=(30,10))

# Titulo do gráfico
plt.title("Analisando as séries mais antigas")

# Ira definir a rotação e o tamanho da fonte
plt.xticks(rotation=90, fontsize=10)

# Ira construir um grafico de pontos com o objetivo de sinalizar o ano de lançamento
# da série, escolhi esse gráfico por que achei mais simples de visualizar, porém
# acredito que não há necessidade da criação de 1, levando em consideração que o filtro
# ja encontrou a série mais antiga
sns.scatterplot(data=titulos_lancados_em_1951, x='Titulo', y= 'Ano de Lançamento')

# Ira exibir o gráfico de pontos
plt.show()

# Impressão das informações da série mais antiga
print("SÉRIE MAIS ANTIGA")
print(titulos_lancados_em_1951)

# Resposta da questão 2: a série mais antiga é a love lucy.


# 3.Séries com avaliação acima de 9: Quantas séries possuem uma 
# avaliação média maior que 9

# Primeiro vou filtrar as séries que possuem a avaliação média
# maior que 9, depois vou verificar o tamanho da coluna para 
# descobrir quantas séries possuem os critérios passados no
# filtro.

series_com_avaliacao_acima_de_9 = len(base_dados_serie.loc[base_dados_serie['Avaliação Media'] > 9])

print("Quantidade de séries que possuem avaliação média ácima de 9: ", series_com_avaliacao_acima_de_9)

# Resposta da questão 3: 39 séries


# 4.Popularidade por genêro: Entre os genêros disponiveis, qual genêro
# possui em média, a maior quantidade de votos?

# primeiro vou verificar qual é o maior numero de votos

votos_em_ordem_crescente = sorted(base_dados_serie['Numero de Votos'])

# para facilitar a visualização no gráfico, vou agrupar os dados 
# por genero e somar o total de votos de cada um

generos_agrupados = base_dados_serie.groupby(by=['Generos'])['Numero de Votos'].sum().reset_index()

generos_agrupados['Generos'] = pd.Categorical(generos_agrupados['Generos'], categories=generos_agrupados['Generos'], ordered=True)


print("Ordem crescente dos votos: ", votos_em_ordem_crescente)

print("GENÊROS MAIS VOTADO")

print(generos_agrupados)


