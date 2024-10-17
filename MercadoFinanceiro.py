

# biblioteca que irá acessar o dataset e manipular os dados
import pandas as pd

# Biblioteca que ira possibiltar reaalizar operações com arrays
import numpy as np

# Biblioteca que ira possibilitar visualizar e manipular gráficos
import matplotlib.pyplot as plt

# Biblioteca que irá possibilitar criar varios tipos de gráficos
import seaborn as sns

# A biblioteca plotly é usada para criar gráficos interativos e visualizações de dados. A sub-biblioteca plotly.graph_objects (importada como go) fornece uma interface de programação orientada a objetos para criar gráficos complexos, permitindo um controle mais detalhado sobre cada elemento do gráfico.
import plotly.graph_objects as go

# Import que ira manipular warnings(mensagens de aviso ao usuário)
# Observação: os warnings não alertam erros fatais ou erros que 
# interrompem a execução do código, eles alertam sobre possiveis
# problemas como comandos depreciados ou práticas desaconselhadas.
import warnings

# Função da biblioteca warning que irá desabilitar os avisos de warning 
warnings.filterwarnings('ignore')

# Acessando a base de dados
base_dados = pd.read_csv('mercadofinanceiro.csv')


# Mostrando as 5 primeiras linhas

print("MOSTRANDO AS 5 PRIMEIRAS LINHAS DO DATAFRAME")
print(base_dados.head())

# Mostrando as informações gerais do dataframe

print("MOSTRANDO AS INFORMAÇÕES GERAIS DO DATAFRAME")

print(base_dados.info())

# Como todos os valores (inclusive os numéricos) são do tipo texto (Object), vamos precisar realizar algumas conversões.

# Transformando a coluna Data em um datetime atraves da função
# to_datetime do pandas
base_dados['Data'] = pd.to_datetime(base_dados['Data'])

# Antes da conversão, devemos substituir as virgulas por pontos. Caso
# contrário a conversão irá dar erro. Vamos fazer usando o metodo
# replace que ira receber 3 paramatros: o valor que será substituido,
# o novo valor e regex=False que irá fazer uma substituição direta,
# ou seja, ele não usará padrões de buscas mais avançados como regras
# para achar numeros, letras, etc.
base_dados['Maior'] = base_dados['Maior'].str.replace(',','.', regex=False)

base_dados['Menor'] = base_dados['Menor'].str.replace(',','.',regex=False)

base_dados['Abertura'] = base_dados['Abertura'].str.replace(',', '.', regex=False)

base_dados['Fechamento'] = base_dados['Fechamento'].str.replace(',','.',regex=False)

# Como os pontos dessa coluna estavam atrapalhando a conversão, resolvi
# substituir os pontos por vázio
base_dados['Volume'] = base_dados['Volume'].str.replace('.','',regex=False)

base_dados['Adj Close'] = base_dados['Adj Close'].str.replace(',', '.',regex=False)

# Metodo que irá converter os valores para float
nova_base_dados = base_dados.astype({'Maior':float, 'Menor':float, 'Abertura':float, 'Fechamento' : float, 'Volume':int, 'Adj Close':float})

# Comando que irá mostrar todas as colunas da tabela
pd.set_option("display.max_columns", None)


# Verificando se a conversão funcionou
print("VERIFICANDO SE A CONVERSÃO FUNCIONOU")

print(nova_base_dados.info())

# Verificando o tamanho do dataset

print("TAMANHO DO DATASET")

print(nova_base_dados.shape)


# Analise descritiva das colunas

print("ANÁLISE DESCRITIVA DAS COLUNAS DO DATASET")

print(nova_base_dados.describe())

# Vamos cosntruir um gráfico de linhas para visualizar melhor os valores
# mas, antes, vamos transformar o nome da coluna em um indice.
# Para isso, vamos utilizar o metodo set_index que recebe como
# parametro a coluna que será transformada em indice, com o
# objetivo de usar as datas como identificadores das linhas. 
dados = nova_base_dados.set_index('Data')

print("VERIFICANDO SE A COLUNA VIROU UM INDICE")

print(dados.head())

# Ira definir o tamanho da imagem do gráfico
plt.figure(figsize = (16,5))

# Ira listar todos os estilos disponiveis da biblioteaca matplotlib
print(plt.style.available)
# Ira adicionar uma sombra no fundo do gráfico
plt.style.use('seaborn-v0_8-darkgrid')
# Irá definir o titulo do gráfico
plt.title("Análise das ações - Fechamento")
# Construindo um gráfico de linhas usando o metodo plot
# da biblioteca matplotlib que irá receber como parametro os 
# valores do eixo x e os valores do eixo y.
# dados.index: Irá pegar os valores do indice da tabela dados,
# no nosso caso, são as datas
# dados['fechamento']: Ira pegar os valores da coluna 'Fechamento'
# Resumindo, vamos criar um gráfico de linhas que ira mostrar como
# os valores da coluna de fechamentos variam ao longo do tempo.
plt.plot(dados.index, dados['Fechamento'])

# Titulo/rótulo do eixo x
plt.xlabel("Periodo da cotação")

# Titulo/rótulo do eixo y
plt.ylabel("Valor da ação (R$)")

# exibição do gráfico
plt.show()


# Verificando os ultimos valores do dataframe

print("ULTIMOS VALORES DO DATAFRAME")

print(dados.tail())
