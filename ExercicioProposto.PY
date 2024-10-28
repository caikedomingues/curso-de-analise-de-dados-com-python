

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

print("QUANTIDADE DE VALORES NULOS")

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

# para facilitar a visualização no gráfico, vou agrupar os dados 
# por genero e somar o total de votos de cada um

generos_agrupados = base_dados_serie.groupby(by=['Generos'])['Numero de Votos'].sum().reset_index()

# vou verificar qual é o maior numero de votos
votos_em_ordem_crescente = sorted(generos_agrupados['Numero de Votos'])

# Descobrindo a maior quantidade de votos
print("Ordem crescente dos votos: ", votos_em_ordem_crescente)

# Filtrando o genero mais votado

genero_mais_votado = generos_agrupados.loc[generos_agrupados['Numero de Votos'] == 8814943]

print("GENERO MAIS VOTADO")

print(genero_mais_votado)

# Resultado da questão 4: a coluna Crime, Drama, Mystery  possui os generos mais votados com 8814943 votos

# 5.Série com mais votos: Qual série possui o maior numero de votos?
# Qual é o seu titulo e avaliação média

# primeiro vamos agrupar os dados por titulo, avaliação média e total de votos.
# O reset_index vai organizar os nossos dados dentro do agrupamento
series_agrupadas = base_dados_serie.groupby(by=['Titulo', 'Avaliação Media'])['Numero de Votos'].sum().reset_index()

# Agora vamos descobrir qual o maior numero de votos dentro do agrupamento.
# Para descobrir essa informação, vamos usar o metodo max.
maior_quantidade_de_voto_da_serie = series_agrupadas['Numero de Votos'].max()

print("MAIOR QUANTIDADE DE VOTOS DO AGRUPAMENTO DE SÉRIES")

print(maior_quantidade_de_voto_da_serie)

# Agora vamos filtrar as informações da série que possui a maior quantidade de votos

serie_mais_votada = series_agrupadas.loc[series_agrupadas['Numero de Votos'] == 2356835]

print("SÉRIE MAIS VOTADA PELO PÚBLICO")

print(serie_mais_votada)

# Resposta da questão 5:
# Titulo da série:  Game of Thrones
# Avaliação Média: 9.2
# Quantidade de votos: 2356835


# 6.Distribuição de lançamentos ao longo dos anos: Quantas séries
# foram lançadas em cada década? (Ex: 1980-1989, 1990-1999, etc)

# Primeiro vou organizar os valores unicos da coluna de anos
# em ordem crescente para podermos visualizar melhor os anos

anos_em_ordem = sorted(base_dados_serie['Ano de Lançamento'].unique())

print("ANOS EM ORDEM CRESCENTE")

print(anos_em_ordem)

# Agora vamos criar os filtros que irão filtrar os anos que irão
# compor o intervalo das decadas

decada_1951_1960 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >= 1951) & (base_dados_serie['Ano de Lançamento'] <= 1960)]

decada_1961_1970 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >= 1961) & (base_dados_serie['Ano de Lançamento'] <= 1970)]

decada_1971_1980 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >=1971) & (base_dados_serie['Ano de Lançamento'] <= 1980)]

decada_1981_1990 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >=1981) & (base_dados_serie['Ano de Lançamento'] <= 1990)]

decada_1991_2000 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >=1991) & (base_dados_serie['Ano de Lançamento'] <= 2000)]

decada_2001_2010 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >= 2001) & (base_dados_serie['Ano de Lançamento'] <= 2010)]

decada_2011_2020 = base_dados_serie.loc[(base_dados_serie['Ano de Lançamento'] >= 2011) & (base_dados_serie['Ano de Lançamento'] <= 2020)]

# Agora vou contar a quantidade de titulos presente en cada decada para descobrir
# quantas séries foram lançadas em cada década
quantidade_titulos_1951_1960 = decada_1951_1960['Titulo'].count()

quantidade_titulos_1961_1970 = decada_1961_1970['Titulo'].count()

quantidade_titulos_1971_1980 = decada_1971_1980['Titulo'].count()

quantidade_titulos_1981_1990 = decada_1981_1990['Titulo'].count()

quantidade_titulos_1991_2000 = decada_1991_2000['Titulo'].count()

quantidade_titulos_2001_2010 = decada_2001_2010['Titulo'].count()

quantidade_titulos_2011_2020 = decada_2011_2020['Titulo'].count()

# Impressão dos resultados
print("QUANTIDADE DE LANÇAMENTOS POR DECADAS")

print("De 1951 á 1960: ", quantidade_titulos_1951_1960)

print("De 1961 á 1970: ", quantidade_titulos_1961_1970)

print("De 1971 á 1980: ", quantidade_titulos_1971_1980)

print("De 1981 a 1990: ", quantidade_titulos_1981_1990)

print("De 1991 á 2000: ", quantidade_titulos_1991_2000)

print("De 2001 á 2010: ", quantidade_titulos_2001_2010)

print("De 2011 á 2020: ", quantidade_titulos_2011_2020)

# Resposta da questão 6

# QUANTIDADE DE LANÇAMENTOS POR DECADAS

# De 1951 á 1960:  6

# De 1961 á 1970:  11

# De 1971 á 1980:  18

# De 1981 a 1990:  52

# De 1991 á 2000:  83

# De 2001 á 2010:  207

# De 2011 á 2020:  464


# 7.Top 5 séries documentárias mais bem avaliadas: Liste as cincos
# séries documentárias mais bem avaliadas, com suas notas e numero de 
# votos.

# Primeiro vamos filtrar o genero "documentário"
genero_documentário = base_dados_serie[base_dados_serie['Generos'] == 'Documentary']

# Agrupamento por titulos, avaliações e total de votos das séries documentais.
series_documentais = genero_documentário.groupby(by=['Titulo', 'Avaliação Media'])['Numero de Votos'].sum().reset_index()

# Agora vamos ordenar os valores em ordem crescente para descobrir os ultimos
# 5 valores (os 5 maiores)
votos_series_documentais_em_ordem = sorted(series_documentais['Numero de Votos'])

print('VOTOS DAS SÉRIES DOCUMENTAIS EM ORDEM')

print(votos_series_documentais_em_ordem)

# 5 maiores valores da coluna de votos: 45186, 48153, 53056, 130608, 161331

# Vamos imprimir no terminal as 5 séries mais votadas e suas informações

# Vamos criar um filtro que irá retornar as informações das séries mais votadas
serie_1_mais_votada = series_documentais.loc[series_documentais['Numero de Votos'] == 161331]

serie_2_mais_votada = series_documentais.loc[series_documentais['Numero de Votos'] == 130608]

serie_3_mais_votada = series_documentais.loc[series_documentais['Numero de Votos'] == 53056]

serie_4_mais_votada = series_documentais.loc[series_documentais['Numero de Votos'] == 48153]

serie_5_mais_votada = series_documentais.loc[series_documentais['Numero de Votos'] == 45186]

# Impressão dos resultados.
print("RANKING DAS 5 SÉRIES DOCUMENTAIS MAIS VOTADAS")

print(serie_1_mais_votada)

print(serie_2_mais_votada)

print(serie_3_mais_votada)

print(serie_4_mais_votada)

print(serie_5_mais_votada)

# Vamos visualizar esses valores graficamente para visualizar melhor os resultados

# Tamanho da imagem do gráfico
plt.figure(figsize=(30,10))

# Titulo do gráfico 
plt.title("Ranking das 5 séries documentais mais votadas")

# Função que ira definir a rotação e o tamanho da fonte do
# eixo x
plt.xticks(rotation=90, fontsize=10)

# Função que irá criar o gráfico de barras. A função recebe como
# argumentos a base de dados análisada, os valores do eixo x e os 
# valores do eixo y
sns.barplot(data=series_documentais, x='Titulo', y='Numero de Votos')

# Exibição do gráfico
plt.show()


# Resposta da questão 7 

# 1° Série: Planet Earth II 
# Numero de votos:   161331
# Avaliação Média: 9.5

# 2° Série: Cosmos: A Spacetime Odyssey
# Número de Votos:  130608
# Avaliação Média: 9.2


# 3° Série: Our Planet
# Número de Votos:  53056
# Avaliação Média: 9.2

# 4° Série: Blue Planet II
# Número de Votos:  48153
# Avaliação Média:  9.3  

# 5° Série: Cosmos
# Número de votos: 45186
# Avaliação Média: 9.3

# 8.Análise de Correlação: Existe alguma correlação entre o ano
# de lançamento e a quantidade de votos? Se sim, qual é o sentido
# dessa correlação?

# Primeiro, vou criar um agrupamento por ano, para realizar a correlção 
# somente das colunas 'Ano de Lançamento' e 'numero de votos'. Vou usar
# o método count para contar a quantidade de votos por ano.
series_por_ano = base_dados_serie.groupby(by=['Ano de Lançamento'])['Numero de Votos'].count().reset_index()

# Após verificar a correlação, vamos verificar os valores em um gráfico de barras
print(series_por_ano.corr())

# Vamos visualizar essa correlação em formato de um gráfico
# de barras

# Irá definir o tamanho do gráfico
plt.figure(figsize=(30,10))

# Irá definir o titulo do gráfico
plt.title("Analisando a quantidade de votos por ano")

# Ira definir a rotação e o tamanho da fonte do eixo x
plt.xticks(rotation=90, fontsize=8)

# Função que irá criar o gráfico de barras: A função irá receber
# como paramtro a base de dados analisada, o valor do eixo x,
# e o valor do eixo y.
sns.barplot(data=series_por_ano, x='Ano de Lançamento', y='Numero de Votos')

# Ira exibir o gráfico
plt.show()

# Resposta da questao 8: Usando o metodo de correlção da biblioteca
# pandas, descobrimos que as 2 colunas tem uma correlação forte positiva,
# Ou seja, as 2 colunas estão fortemente correlacionadas. Ao analisar
# o gráfico de barras, podemos perceber que, conforme vai se passando
# os anos, o numero de votos vai aumentando, tendo 2019 como o ano que
# possui o maior número de votos.
# Acredito que isso ocorra por conta do avanço técnologico que possibilitou uma expansão dos metodos de coleta de informações
# além de aprimorar a maneira como o público transmite as suas 
# opiniões e votações.

# valor do método da correlação: 0.826579 

# 9: Relação entre número de votos e avaliação média: Para séries
# com mais de 500.000 votos, qual a média da avaliação média

# Primeiro vou filtrar as séries que possuem mais de 500.000
# votos

series_com_mais_de_500 = base_dados_serie.loc[base_dados_serie['Numero de Votos'] > 500.000]

# Agora vamos usar a função mean para descobrir a média dos valores
# da coluna 'Avaliação Média' da variável series_com_mais_de_500
# que recebe a base de dados filtrada com os valores que precisamos.

print("MÉDIA DAS AVALIAÇÕES MÉDIAS DAS SÉRIES QUE POSSUME MAIS DE 500.000 VOTOS")
print(series_com_mais_de_500['Avaliação Media'].mean())

# Resposta da questão 9: A média das avaliações médias das séries que possuem 
# mais de 500.000 votos é 8.3675



# 10. Gêneros de maior audiência: Quais são os três generos mais 
# recorrentes nas séries com mais de avaliação média maior que 8?

# Primeiro vou filtrar as séries que possuem média maior que 8.

series_com_media_maior_que_8 = base_dados_serie.loc[base_dados_serie['Avaliação Media'] > 8]

# Agora vou agrupar os dados por genero e avaliação média.

# size: Esse método conta o número de ocorrências em cada grupo. Por exemplo, se houver 5 séries de um determinado gênero com a mesma avaliação média, o size() retorna 5 para esse grupo específico.
series_agrupadas_por_genero = series_com_media_maior_que_8.groupby(by=['Generos', 'Avaliação Media']).size().reset_index()

# Agora vou analisar a porcentagem de frequencia dos generos em cada titulo
print("GÊNEROS MAIS RECORRENTES EM SÉRIES COM AVALIAÇÃO MÉDIA MAIOR QUE 8")

# Vamos calcular a frequência usando a função value_counts que ira receber
# como parametro o normalize True, que irá calcular a porcentagem de 
# frequência dos gêneros
print(series_agrupadas_por_genero['Generos'].value_counts(normalize=True) * 100)

# Resposta da questão 10:

# 1° Genero: Drama
# Ocupa 3% dos dados

# 2° Genero: a coluna de Action, Adventure, Animation     
# ocupam 2.79% dos dados

# 3° Genero: a coluna de  Crime, Drama, Thriller  

# Também ocupam 2.79% dos dados

# 11. Top 10 séries mais recentes e bem avaliadas: Liste as 10 séries
# mais recentes com avaliação acima de 8.

# Primeiro vou filtrar as séries de 2024 com avalições maiores que 8

series_de_2024_com_avaliacao_maior_que_8 = base_dados_serie.loc[(base_dados_serie['Avaliação Media'] > 8) & (base_dados_serie['Ano de Lançamento'] == 2024)]

# Agora vou criar um gráfico de barras para criar um ranking com essas séries 

# Irá definir o tamanho da imagem do gráfico
plt.figure(figsize=(30,15))

# Ira definir o titulo do gráfico
plt.title("Séries de 2024 com avaliações maiores que 8")

# Ira definir a rotação e o tamanho da fonte do eixo x
plt.xticks(rotation=90, fontsize=10)

# Ira criar o gráfico de barras. A função recebe como argumento a base de dados, o valor do
# eixo x e o valor do eixo y
sns.barplot(data=series_de_2024_com_avaliacao_maior_que_8, x = 'Titulo', y = 'Avaliação Media')

# Exibição do gráfico
plt.show()

# Agora vamos agrupar esses dados por titulo e avaliação para podermos 
# imprimir na tela o resultado de suas avaliações, que tornará ainda mais
# fácil a montagem do rank

series_2024_agrupadas = series_de_2024_com_avaliacao_maior_que_8.groupby(by=['Titulo', 'Avaliação Media']).size().reset_index()

# Agora vamos ordenar em ordem decrescente as avaliações médias para podermos organizar melhor
# o ranking das séries
print(sorted(series_2024_agrupadas['Avaliação Media'], reverse=True))

# Exibição das séries e sua votações
print("SÉRIES DE 2024 COM AVALIAÇÕES MÉDIAS MAIORES QUE 8")

print(series_2024_agrupadas)

# 1° Lugar: The penguin e x-men 97
# Avaliação Média: 8.8

# 2° Lugar: Shogun e Very PariVarik
# Avaliação Média: 8.6

# 3° Lugar: Mr Bates vs. The Post Office
# Avaliação Média: 8.5

# 4° Lugar: fallout
# Avaliação Média: 8.4

# 5° Lugar: Kaiju No. 8  e Solo Leveling 
# Avaliação Média: 8.3

# 6° Lugar: Queen of Tears    
# Avaliação Média: 8.2

# 7° lugar: One Day e Ripley      
# Avaliação Média: 81.

# Observação, como podemos observar no gráfico, em 2024, as séries
# com avaliação acima de 8, não alcançaram a nota 9.


