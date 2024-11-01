
# Conjunto de dados de vendas de videogames: Dados de vendas e classificações de jogos de videogame extaridos do VZCharts.

# Import das bibliotecas necessárias para a análise

# Biblioteca que irá acessar o dataset para possibilitar
# a manipulação e a análise dos dados
import pandas as pd

# Biblioteca que possibilita manipular arrays
import numpy as np

# Biblioteca que ira possibilitar manipular gráficos
import matplotlib.pyplot as plt

# Biblioteca que ira possibiklitar criar gráficos personalizados
# usando a classe graph_objects
import plotly.graph_objects as go

# import da biblioteca seaborn que contém uma grande variedade de gráficos

import seaborn as sns

# import da biblioteca que manipula / administra warnings

import warnings

# Função que irá desabilitar os warnings

warnings.filterwarnings('ignore')


# Acessando/lendo o dataset que será utilizado na análise
# latin-1: especifica o tipo de codificação dos caracteres
# usados para ler o arquivo csv. Essa codificação é um padrão
# para caracteres acentuados, usados em linguas como o portugues
# espanhol, frânces, entre outras.
# Nesse caso específico, a leitura pode não funcionar corretamente sem  essa codificação, pois caracteres especiais podem ser exibidos de forma incorreta.
base_dados = pd.read_csv('Games.csv', encoding='latin-1')


# Metodo que irá possibilitar que todas as colunas sejam mostradas
pd.set_option("display.max_columns", None)

# Ira mostrar as 5 primeiras linhas
print("VISUALIZANDO AS 5 PRIMEIRAS LINHAS DA BASE DE DADOS")
print(base_dados.head())

# Informações gerais do dataset

print("INFORMAÇÕES GERAIS DO DATASET")

print(base_dados.info())


# Analisando a dimensão (tamanho) da base de dados, a função irá
# retornar 2 valores: o numero de linhas e o numero de colunas.
print("DIMENSÃO DA BASE DE DADOS")

print(base_dados.shape)


# Renomeando as colunas do dataset

base_dados.rename(columns={
    
    
        'Game':'Jogo',
        'Year': 'Ano',
        'Genre': 'Genero',
        'Publisher':'Editora',
        'North America': 'America do Norte',
        'Europe': 'Europa',
        'Japan':'Japao',
        'Rest of World':'Resto do mundo'
}, inplace=True)

# Verificando se os nomes foram alterados

print("Verificando a renomeação das colunas")

print(base_dados.columns)

# Verificando a quantidade de valores nulos na tabela

print("QUANTIDADE DE VALORES NULOS")

print(base_dados.isnull().sum())

# Verificando os valores nulos de forma gráfica usando o heatmap (mapa
# de calor).

# Ira configurar o tamanho do gráfico
plt.figure(figsize=(14,6))

# Ira criar o titulo do gráfico
plt.title("Verificando os valores nulos de forma gráfica")

# Ira criar o grafico de calor: A função ira receber como parametro
# a função isnull do pandas
sns.heatmap(base_dados.isnull())

# Exibição do grafico
plt.show()

# Após a verificação dos valores, vamos apagar os valores nulos
# da tabela usando a função dropna(), que ira receber como parametro
# as colunas que terão suas linhas nulas excluidas.
# É necessário passar o parametro inplace = True para garantir
# que a modificação seja feita no dataset original.
base_dados.dropna(subset=['Ano'], inplace=True)

base_dados.dropna(subset=['Editora'], inplace=True)

print("VERIFICANDO SE OS VALORES NULOS FORAM APAGADOS")

print(base_dados.isnull().sum())

print("VERIFICANDO A DIMENSÃO DA BASE DE DADOS APÓS A EXCLUSÃO DE VALORES NULOS ")

print(base_dados.shape)

# Descrição analitica da base de dados

print("DESCRIÇÃO ANÁLITICA DA BASE DE DADOS")

print(base_dados.describe())

# Vamos criar um gráfico de barras usando a biblioteca seaborn.
# A função barplot que cria os gráficos irá receber como parametro
# a base de dados, os valores do eixo x e os valores do eixo y.

#ira criar o titulo do gráfico que ficara alinhado a esquerda e 
# terá tamanho 14
plt.title("Quantidade de vendas globais(mi)", loc= 'left', fontsize=14)

plt.figure(figsize=(10,5))

# Rótulo do eixo Y
plt.ylabel("Quantidade de vendas")

# Irá criar o gráfico de barras
# c1 = None: Desabilita a exibição dos intervalos de confiança. Apenas as barras são exibidas, sem linhas de erro.
# Color: ira definir a cor das barras do gráfico.
# Estimator: No Seaborn, o parâmetro estimator no método barplot permite que você defina qual função será aplicada aos dados numéricos para gerar os valores representados pelas barras.
# Por padrão, o barplot usa a média (mean) dos valores como estimador. No entanto, você pode usar qualquer outra função agregadora, como a soma (sum), contagem (len), mediana (median), etc.
sns.barplot(data=base_dados, x = 'Ano', y='Global', ci=None, color='#69b3a2', estimator=sum)

# Exibição do gráfico
plt.show()

# Como os anos 2019 e 2020 não tiveram vendas, vamos retirar eles da coluna de anos. Para isso, vamos usar o comando loc para filtrar
# os anos (2019, 2020) com o intuito de não mostrar mais eles na 
# base de dados

# Basicamente, vamos passar como condição do loc, todos os valores 
# diferentes de 2019 e 2020 com o objetivo de remover esses anos 
# da base de dados
base_dados = base_dados.loc[(base_dados['Ano'] != 2019) & (base_dados['Ano'] != 2020)]

print("VERIFICANDO SE OS ANOS 2019 E 2020 FORAM OCULTADOS")

print(base_dados['Ano'].unique())


# Agora vamos analisar a distribuição dos dados da coluna 'Global'
# usando um grafico kdeplot da biblioteca seaborn
# kdeplot: Serve para visualizar a de uma variável continua, mas 
# em vez de mostrar barras, ele desenha uma linha que representa
# a densidade de probabilidade dos dados.

# Ira configurar o tamanho da imagem do gráfico
plt.figure(figsize=(12,5))

# irá definir o titulo do gráfico alinhado a esquerda com tamanho 14

plt.title('Distribuição das vendas globais', loc='left', fontsize=14)

# Ira adicionar grades no fundo gráfico
plt.style.use('ggplot')

# função que irá construir o kdeplot da coluna 'Global'
# shade: Este argumento preenche a área abaixo da curva
# de densidade com uma cor.
# bw: irá definir a largura da banda(suavização da curva de densidade no gráfico.) o que pode afetar as variações dos dados
# color: Define a cor da curva
# linewidth: define a largura da linha.
sns.kdeplot(base_dados['Global'], shade=True, bw=1, color='#96a8a8', linewidth=2.5)

# Irá definir o rótulo do eixo y
plt.ylabel('Densidade')

# Irá exibir o gráfico
plt.show()


# Verificando o total de vendas por ano: Para realizar essa ação,
# vamos agrupar os dados por ano e calcular o total de valores em
# cada coluna.

print("VENDAS POR ANO")

print(base_dados.groupby(by=['Ano']).sum())


# Visualiando a distribuição global por ano usando o boxplot da 
# biblioteca seaborn

# Irá definir o tamanho do gráfico
plt.figure(figsize=(10,5))

# Irá definir o titulo do gráfico
plt.title("Distribuição das vendas globais por ano")

# Rótulo do eixo x
plt.xlabel("Vendas globais")

# Função que irá criar o boxplot, ela ira receber como a parametro
# a base de dados com os valores, os valores do eixo x(ano) e os
# valores do eixo y(Vendas globais).
sns.boxplot(data=base_dados, x = 'Ano', y = 'Global')

# Exibição do gráfico
plt.show()

# Vamos usar a função loc para visualizar valores maiores ou iguais
# a 10 (milhões) da coluna 'global'

print("VISUALIZANDO VALORES MAIORES OU IGUAIS A 10 NA COLUNA DE VENDAS GLOBAIS")

# Função que irá filtrar os valores maiores ou iguais a 10
print(base_dados.loc[(base_dados['Global'] >= 10)])


# Verificando o total de vendas por ano
print("VERIFICANDO O TOTAL DE VENDAS POR ANO")
# Ira trazer o total de vendas de cada coluna por ano. essa variável
# será utilizada no cálculo de porcentagem de vendas, já que ela 
# retorna o valor total de vendas por região
analise = base_dados.groupby(by=['Ano']).sum().reset_index()

print(analise)


# analisando a proporção dos 100% de cada região comparado ao Total

# Aqui o código esta criando uma lista de porcentagens de vendas para 
# cada região, com o objetivo de comparar as vendas regionais com as
# vendas globais. O for irá percorrer as colunas com o objetivo de 
# criar pares de valores (vendas regionais, vendas globais) usando a função zip.
# Função zip: Tem como objetivo juntar 2 listas ou colunas, ou seja,
# o Python vai "emparelhar" o primeiro valor de vendas_america com o 
# primeiro valor de vendas_globais, o segundo com o segundo, e assim por diante.
# Dentro da lista também teremos o cálculo da porcentagem
america = [america / total * 100 for america, total in zip(analise['America do Norte'], analise['Global'])]

europa = [europa / total * 100 for europa, total in zip(analise['Europa'], analise['Global'])]

japao = [japao / total * 100 for japao, total in zip(analise['Japao'], analise['Global'])]

mundo = [mundo / total * 100 for mundo, total in zip(analise['Resto do mundo'], analise['Global'])]


print("PORCENTAGEM DA AMERICA DO NORTE NAS VENDAS GLOBAIS")

print(america)

print("PORCENTAGEM DA EUROPA NAS VENDAS GLOBAIS")

print(europa)

print("PORCENTAGEM DO JAPÃO NAS VENDAS GLOBAIS")

print(japao)

print("PORCENTAGEM DO RESTO DO MUNDO NAS VENDAS GLOBAIS")

print(mundo)

# Criando um grafico de barras empilhadas usando o matplotlib

# barras: compara a distribuição das vendas em quatro regiões (América do Norte, Europa, Japão e Resto do Mundo) ao longo de diferentes anos. Cada barra representa a soma total das vendas, enquanto as diferentes camadas dentro da barra mostram a contribuição de cada região para o total.

# Tamanho da imagem do gráfico
plt.figure(figsize=(10,5))

# Largura da barra no gráfico
largura_barra = 0.85

# Extrai os rótulos para o eixo x
rotulos = analise['Ano']

# Define os grupos para o eixo x. Cada número representa uma posição
# onde uma barra será desenhada. Esses numeros devem corresponder ao
# número de anos que nós temos no dataframe.
grupos = [0, 1, 2, 3, 4, 5]

# Titulo do gráfico
plt.title("Análise de distribuição por continentes")

# Plotagens dos valores nas barras

# 1° camada da barra: representa as vendas da américa do norte e a função
# bar irá receber como parametro: o width que é a largura da barra, o 
# color que é a cor da primeira camada da barra e o edgecolor que é a cor
# da borda das barras
plt.bar(grupos, america, width=largura_barra, color='#b5ffb9', edgecolor='white')

# 2° camada da barra: Representa as vendas da Europa e a função bar 
# recebe como parametro: o bottom que indica que essas barras começam
# onde as barras da america terminam, que resulta em um gráfico de 
# barras empilhado, o color define a cor da segunda camada e o edgecolor
# irá definir a cor da borda da barra.
plt.bar(grupos, europa, bottom=america, width=largura_barra, color='#f9bc86', edgecolor='white')

# 3° camada da barra: representa as vendas do japao e a função bar recebe
# como paremetro: o bottom que irá especificar que essas barras começam
# onde as barras da america e da europa terminaram, o color define a cor
# da camada e o edgecolor define a cor da borda da barra
plt.bar(grupos, japao, bottom=[a + b for a, b in zip(america, europa)], width=largura_barra, color = '#a3acff', edgecolor='white')

# 4° camada da barra: representa as vendas do resto do mundo e a função bar ira receber como parametro, o bottom que indica que a barra irá
# começar onde as barras da america, europa e japão terminaram, o 
# color ira definir a cor da camada e o edcolor a cor da borda da barra
plt.bar(grupos, mundo, bottom=[a + b + c for a, b, c in zip(america, europa, japao)], width=largura_barra, color='#d3acfe', edgecolor='white')

# Observação: as funções bar também irão receber como parametro os valores dos eixos x e y

# Define as posições do eixo x (grupos) e atribui os rótulos correspondentes (rotulos). Isso garante que cada grupo tenha um rótulo correspondente ao ano ou categoria.
plt.xticks(grupos, rotulos)

# Rótulo do eixo x
plt.xlabel('Grupo')

# Rótilo do eixo y
plt.ylabel('Distribuição (%)')

# : Adiciona uma legenda ao gráfico. A lista define os rótulos da legenda para cada uma das camadas de barras.

# loc='upper left' posiciona a legenda no canto superior esquerdo.
# bbox_to_anchor=(0.15, -0.1) ajusta a posição da legenda em relação à figura.
# ncol=4 define que a legenda deve ter quatro colunas.
plt.legend(['America N', 'Europa', 'Japão','Mundo'], loc='upper left', bbox_to_anchor = (0.15, -0.1), ncol=4)

# Exibe o gráfico
plt.show()


# Vamos dar uma analisada nas empresas que publicaram os jogos usando
# a função unique que irá retornar os valores únicos das colunas 

print("VERIFICANDO OS VALORES UNICOS SA COLUNA EDITORA")

print(base_dados['Editora'].unique())

# Como podemos perceber, há uma enorme quantidade de editoras na coluna
# o que pode, em alguns momentos, dificultar as nossas análises, já que
# os dados da coluna são do tipo texto, logo, é interessante transformamos esses valores em valores quantitativos, por exemplo, 
# a rockstar irá passar a ser 1, a activision 2 e assim por diante

# import da biblioteca sklearn que irá permitir a utilização
# da classe labelencoder que irá poder transformar dados
# categóricos (textos) em valores numéricos.
from sklearn.preprocessing import LabelEncoder

# criação do objeto labelEncoder
funcao_rótulo = LabelEncoder()

# Variável que ira conter a função fit_transform que irá aprender
# sobre os dados da coluna editora e transforma-los em numeros
editora_transformada = funcao_rótulo.fit_transform(base_dados['Editora'])

# Verificando a transformação 
print("VERIFICANDO SE A TRANSFORMAÇÃO DA COLUNA EDITORA FOI REALIZADA COM SUCESSO")
print(editora_transformada)


# Agora vamos criar uma nova coluna na base de dados que irá conter
# os valores que representam as editoras

base_dados['codigo_editora'] = editora_transformada

# Verificando se a coluna foi criada

print("VERIFICANDO SE AS COLUNA CODIGO DA EDITORA FOI CRIADAS")

print(base_dados.columns)

# Agora cada editora possui um código de identificação

# Agora vou fazer a mesma coisa com as colunas 'jogo' e 'genero'

# Transformando as colunas 'jogo' e 'genero' em rótulos
jogo_transformado = funcao_rótulo.fit_transform(base_dados['Jogo'])

genero_transformado = funcao_rótulo.fit_transform(base_dados['Genero'])

# Criando as colunas que irão conter os códigos 

base_dados['codigo_jogo'] = jogo_transformado

base_dados['codigo_genero'] = genero_transformado

# Agora vamos verificar se as colunas foram criadas

print("VERIFICANDO SE AS COLUNAS FORAM CRIADAS")

print(base_dados.columns)


# A biblioteca seaborn, também permite trabalhar com paletas de cores
# Usando a função color_palette, que recebe como parametro o tipo
# da paleta e a quantidade de cores.

paleta_cores = sns.color_palette('husl', 8)

print("MOSTRANDO A PALETA DE CORES")

print(paleta_cores)

# Agora, vamos usar a nossa paleta de cores em um gráfico scatterplot
# da biblioteca seaborn

# Scatterplot(gráfico de dispersão): É utilizado para visualizar a relação entre 2 variáveis continuas, plotando pontos em um gráfico. 
# Ele é muito útil para observar padrões, correlações, tendências ou agrupamentos nos dados

# Irá definir o titulo do gráfico
plt.title('Análise dos produtores de games(mi)')

# Ira definir o tamanho da imagem do gráfico
plt.figure(figsize=(20,5))

# A função que irá construir o gráfico deve receber como argumento
# a base de dados, o valor do eixo x, o valor do eixo y e o indice
# da cor da paleta que queremos utilizar no gráfico

sns.scatterplot(data=base_dados, x='codigo_editora', y='Global', color=paleta_cores[0])

#Exibição do gráfico
plt.show()

# Também podemos verificar qual gênero vendeu mais usando um scatterplot

# Tamanho do gráfico
plt.figure(figsize=(20,5))

# titulo do gráfico
plt.title('Análise dos genêros de games(mi)')

# Função que ira criar o scatterplot dos generos de jogo
sns.scatterplot(data=base_dados, x = 'codigo_genero', y = 'Global', color=paleta_cores[0])

# Exibição do gráfico
plt.show()

# Análise dos games mais vendidos usando o scatterplot

# Titulo do gráfico
plt.title('Análise dos games(mi)')

# Tamanho da imagem do gráfico
plt.figure(figsize=(20,5))

# Função que ira criar o scatterplot dos jogos
sns.scatterplot(data=base_dados, x='codigo_jogo', y = 'Global', color=paleta_cores[0])

# Exibição do gráfico
plt.show()


# Report gerencial: vamos criar um relatório usando matplotlib
# que será baseado em todas as nossas análises feitas anteriormente

# Primeiro vamos definir o tamanho da imagem do gráfico
# de cada subplot
fig, ax = plt.subplots(figsize=(40,30))

# Quantidade de colunas
colunas = 3

# quantidade de linhas
linhas = 2

# cor de fundo dos gráficos
cor_fundo = '#f5f5f5'

# Ira aplicar a cor de fundo nos gráfiocs
ax.set_facecolor(cor_fundo)
fig.set_facecolor(cor_fundo)

# estilo dos graficos
plt.style.use('seaborn-v0_8')

# Ira definir o a quantidade de linhas, colunas e a posição 
# que queremos acessar
plt.subplot(linhas, colunas, 1)
plt.title('Gráfico 1')

plt.subplot(linhas, colunas, 2)
plt.title('Gráfico 2')

plt.subplot(linhas,colunas, 3)
plt.title('Gráfico 3')

plt.subplot(linhas, colunas, 4)
plt.title('Gráfico 4')

plt.subplot(linhas, colunas, 5)
plt.title('Gráfico 5')

plt.subplot(linhas, colunas, 6)
plt.title('Gráfico 6')

plt.show()

# Irá listar os estilos de gráficos disponiveis
print(plt.style.available)