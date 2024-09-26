

# Histogramas
# um histograma é um tipo de gráfico que representa a distribuição de uma # variável contínua ou discreta, mostrando como os valores dessa variável # estão distribuídos em diferentes intervalos ou bins (caixas). Na 
# análise de dados, o histograma é amplamente utilizado para visualizar a # frequência de ocorrências de valores dentro desses intervalos, # permitindo que os analistas identifiquem padrões como tendências, dispersão, simetria, e outliers.


# Import das bibliotecas
import numpy as np

import matplotlib.pyplot as plt

# Ira gerar dados aleatórios a partir de uma distribuição normal
# (ou Gaussiana), que é caracterizada por uma curva em forma de 
# sino.
# parametros do normal
# 10: é a média dos dados, ou seja, o valor central
# em torno da distribuição dos dados
# 0.5: é o desvio padrão que controla a dispersão dos dados em
# torno da média. Quanto menor o desvio padrão, mais concentrados
# os dados ficam em torno da média.
# 5000: é o numero de pontos dados gerados, ou seja, um conjunto
# de 5000 numeros aleatórios será criado
data = np.random.normal(10, 0.5, 5000)

# Cria um histograma e recebe como parametro os dados gerados
plt.hist(data)

# Exibição do histograma
plt.show()


# Boxplot
# É uma ferramenta estatistica utilizada na analise de dados para
# visualizar a distribuição de uma variável. Ele oferece uma maneira
# simples e eficiente de mostrar informações sobre a dispersão, assimetria, valores extremos(outliers) e resumo estatistico de um
# conjunto de dados.

# 1.caixa(Box):

# Quartil Inferior(Q1): Marca o valor onde 25% dos dados estão abaixo
# desse ponto.

# Quartil Superior(Q3): Marca o valor onde 75% dos dados estão abaixo
# desse ponto.

# A caixa vai de Q1 até Q3, representando os 50% centrais dos dados.

# 2.Mediana:
# A linha do meio na caixa representa a mediana(Q2), ou seja, o valor onde 50% dos dados estão abaixo e 50% dos dados estão ácima. Ela é 
# o ponto central dos dados

# 3.Bigodes:
# os bigodes se estendem a partir da caixa até o menor e maior valor que não são considerados outliers.

# 4.Outliers:
# Os valores outliers são aqueles que estão muito distantes do restante dos dados, fora do intervalo de bigodes, e são marcados como pontos
# individuais no gráfico.
plt.boxplot(data)

plt.show()

# scatterplot(gráfico de dispersão): Serve para visualizar a relação entre 2 variáveis numéricas ele plota um ponto para cada par de valores correspondentes as 2 variáveis(eixo x, eixo y)

# Eixo x(Horizontal): representa os valores de uma variável
# Eixo y(vertical): Representa os valores de outra variável
# Pontos de dispersão: cada ponto no gráfico representa um
# par de valores(X,Y), ou seja, uma observação dos dados.


# Gera 100 numeros aleatórios seguindo uma distribuição normal com
# média 10 e desvio padrão 0.5. Isso cria uma sequencia de numeros
# que se agrupam em torno de 10 com pequenas variações
x = np.random.normal(10, 0.5, 100)

# Gera outro conjunto de 100 valores aletórios, mas com uma média de 0
# e desvio padrão de 20, criando valores mais dispersos e com maior
# variabilidade.
y = np.random.normal(0, 20, 100)

# Cria uma nova figura (tela onde os graficos são apresentados) 
fig = plt.figure()

# Cria um sistema de eixos, que nos permite adicionar elementos ao grafico
ax = plt.axes()

# Plota um gráfico de dispersão usando as variáveis x e y
# marker: define o formato dos pontos
# color: define a cor dos pontos
# label: atribui um rótulo a legenda
# alpha: define a transparência dos pontos
ax.scatter(x, y, marker='o', color='red', label='data 1', alpha=0.5)

# Plota o segundo conjunto dos dados, aqui os valores de x e y são 
# escalados pela metade (multiplicados por 0.5) então os pontos estarão em posições mais próximas da origem(0,0) e o gráico mostrará essa redução

# marker: define o formato dos pontos
# color: define a cor dos pontos
# label: define o rótulo que será exibido na legenda
# alpha: define a transparencia dos pontos (acho que de 0 a 1)
ax.scatter(x*0.5, y*0.5, marker='o', color='black', label='data 2', alpha=0.7)

# Serve para adicionar a leegenda no grafico e mostrará o nome dos 
# rótulos para podermos distinguir os 2 conjuntos de pontos
ax.legend()

# Exibição do gráfico
plt.show()

# Biblioteca plotly.express: é uma ferramenta de visualização de dados
# que permite a criação rápida de gráficos interativos e estatisticos
import plotly.express as px

# Esse comando serve para acessar um dataset(conjunto de dados) interno
# do plotly express chamado gapminder. Esse conjunto de dados contém
# informações sobre diversos paises como: pais(country), continente(continent), ano(year), expectativa de vida(lifeExp), população(pop),
# pib per capita(gdpPercap), ISO code(iso_alpha, iso_num)-codigo ISO de cada pais
print(px.data.gapminder())

# Vamos filtrar as informações do dataset e pegar apenas dados referentes
# ao Brasil

# Vamos usar o pandas para utilizar a função query
import pandas 

# Irá filtrar os dados para carregar apenas as informações relacionadas
# ao Brasil. o set index define a coluna 'year' como indice do dataframe.
# Isso significa que a coluna 'year' se tornara o indice principal, 
# permitindo que você acesse os dados por ano com facilidade.
df = px.data.gapminder().query('country == "Brazil"').set_index('year')

print("5 PRIMEIRAS LINHAS DOS DADOS DO BRASIL")
print(df.head())


# Grafico de linhas sobre o pib per capita do brasil

# Comando para a criação do gráfico de linha a função plot recebe 2
# argumentos, o primeiro é os valores de x e o segundo é os valores 
# de y, no nosso caso, como definimos o year como indice, vamos passar
# os valores de year como x e os valores da coluna per capita como y
# df.index: retorna  os valores do indice do dataframe (coluna year)
plt.plot(df.index, df['gdpPercap'])
# Titulo do gráfico
plt.title('PIB per capita do Brasil')
# Titulo dos rótulos x e y
plt.ylabel('PIB per capita')
plt.xlabel('Tempo')

plt.show()

# Grafico de dispersão que irá mostrar a relação entre a expectativa
# de vida e renda per capita do brasil
# Ira criar uma nova tela e configurar o tamanho da imagem(largura e altura)
plt.figure(figsize=(12,4))

# Ira atribuir ao eixo x a expectativa de vida e ao eixo y
# o pib per capita
plt.scatter(df['lifeExp'], df['gdpPercap'])
# Rótulo dos eixos x e y
plt.xlabel('Expectativa de vida')
plt.ylabel('Renda per capita')

# Titulo do grafico com alinhamento a esquerda
plt.title('Relação entre expectativa de vida e renda per capita no brasil', loc='left')
# Exibição do gráfico
plt.show()

# Gráfico de barras sobre a quantidade de pessoas no brasil(população)
# Plt bar: Usado para criar o gráfico de barras
# o eixo x ira conter os indices, e o y(height, que irá referencia ao valores que irão aparecer nas barras)
# color: define a cor das barras
plt.bar(x = df.index, height=df['pop'], color='red')

# title: titulo dos gráficos
plt.title('População Brasileira')

# Exibição do gráfico
plt.show()


# Essa função terá como objetivo filtrar os dados de um continente em
# especifico do dataframe. 
def filtrar_continente(continente):

     # ira carregar o dataset
    df = px.data.gapminder()
    
    # Ira filtrar os continentes do dataframe
    df = df[df['continent'] == continente]
    
    # ira retornar o continente informado
    return df


def filtrar_pais(pais):
    
    # ira carregar o dataset
    df = px.data.gapminder()
    
    # Ira filtrar os paises do dataframe
    df = df[df['country'] == pais]

    # Ira retornar o pais informado
    return df

# Filtra os continentes ('Americas' no nosso caso)
americas = filtrar_continente('Americas')
# lista única dos paises do continente
paises = americas['country'].unique()

# Ira gerar a tela onde grafico aparecerá e definira o tamanho da imagem
plt.figure(figsize=(12,8))

# For que irá percorrer os paises do continente para plotar
# os valores nos eixos
for pais in paises:
    # Ira filtrar os paises
    df_pais = filtrar_pais(pais)
    
    # ira criar o scatterplot(gráfico de dispersão)
    # o eixo X terá os valores das expectativas de vida
    # o eixo y terá o valores dos pib per capita
    plt.scatter(df_pais['lifeExp'], df_pais['gdpPercap'])

# Adiciona a legenda com o nome dos paises, o best irá posicionar
# automaticamente a legenda no local que o sistema considerar mais
# apropriado
plt.legend(labels = paises, loc='best')
# Titulo do gráfico com alinhamento a esquerda
plt.title('Relação entre renda per capita e expectativa de vida',loc='left')
# Titulo / rótulos dos eixos x e y
plt.xlabel('Expectativa de vida')
plt.ylabel('Renda per capita')
# Exibição do gráfico
plt.show()
