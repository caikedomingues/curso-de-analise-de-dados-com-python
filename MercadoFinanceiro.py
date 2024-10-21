

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

# O trecho dados['Fechamento'].rolling(5) cria uma "janela móvel" de 5 
# períodos sobre a coluna 'Fechamento' do DataFrame dados.
# Isso significa que ele está preparando uma análise de médias ou cálculos baseados nos últimos 5 valores de cada ponto da série de dados. A função rolling(5) não realiza o cálculo por si só, mas cria um objeto que permite calcular estatísticas como média, soma, desvio padrão, etc., para cada janela de 5 linhas consecutivas.
# Resumindo ele ira criar uma janela que se move sobre os dados a cada
# 5 valores.

# Para análisar melhor, vamos criar 2 variáveis, uma que irá conter
# média móvel e outra que ira conter a média tendência
print("CALCULO DA MÉDIA APÓS 5 VALORES")

# media com intervalo de 5 dias 
media_movel = dados['Fechamento'].rolling(5).mean()


print("CALCULO DA MÉDIA APÓS 30 DIAS")
# média com intervalo de 30 dias
media_tendencia = dados['Fechamento'].rolling(30).mean()


# Agora, vamos plotar esses valores em um gráfico de linhas

# Ira adicionar uma sombra (grade) no fundo do gráfico
plt.style.use('seaborn-v0_8-darkgrid')

# Ira configurar o tamanho da imagem do gráfico
plt.figure(figsize=(16, 5))

# Ira criar o titulo do gráfico
plt.title("Análise das ações da magalu - fechamento")

# plotagem / inserção dos valores no gráfico. A função plot
# ira receber 2 parametros: os valores do exio x e os valores
# eixo y.

# Valores de x: irá receber os indices (datas) das cotações

# valores de y: irá receber como  parametro o valor das cotações
plt.plot(dados.index, dados['Fechamento'])

plt.plot(dados.index, media_movel)

plt.plot(dados.index, media_tendencia)

# Rótulo / titulo do eixo x
plt.xlabel("Periodo da Cotação")

# Rótulo / titulo do eixo y
plt.ylabel("Valor da ação")

# Exibição do gráfico.
plt.show()


# Também é possivel verificar os dados usando um boxplot da biblioteca
# seaborn, que ira receber como parametro 2 valores: a base de dados
# e o valor do eixo x
sns.boxplot(data=dados, x = 'Fechamento')

# Exibição do gráfico
plt.show()


# Vamos melhorar essa visualização criando um boxplot mensal

# Primeiro, vamos criar uma nova coluna na base de dados que irá
# armazenar os meses da coluna Data. Como a coluna Data é uma
# coluna do tipo datetime, podemos usar a função month para 
# capturar os meses da coluna.

# Criação da coluna 'mes'

base_dados['mes'] = base_dados['Data'].dt.month

# Verificando se a coluna foi criada com sucesso
print("VISUALIZANDO A COLUNA DE MESES")

print(base_dados.head())

# Construção do boxplot usando a biblioteca seaborn.
# A função irá receber como parametro a base de dados, os valores de x
# (meses)  e os valores de y(valor do fechamento)

# Ira configurar o tamanho da figura do gráfico
plt.figure(figsize=(16,5))

# Função que irá criar o boxplot
sns.boxplot(data=base_dados, x = 'mes', y = 'Fechamento')

# Exibição do gráfico
plt.show()


# Também é interessante agrupar os valores por mes, para descrever
# analiticamente os valores de fechamento em cada mes

print("ANALISANDO OS VALORES DE FECHAMENTO POR MES USANDO UM AGRUPAMENTO")

# Vamos agrupar os dados por mes e descrever os valores da Fechamento
# em cada mes.
print(base_dados.groupby(by=['mes'])['Fechamento'].describe())


# Por fim, vamos crir um gráfico candlestick: O grafico candlestick
# é amplamente utilizado para representar o comportamento de preços
# de um ativo(como ações, criptomoedas ou commodities) durante um 
# periodo de tempo especifico, geralmente em análise técnica

# Função da biblioteca plotly que irá criar o gráfico candlestick

# Função que cria um objeto gráfico vázio no qual você pode adicionar
# diferentes tipos de gráficos. Neste caso, você está criando uma
# figura que conterá gráfico candlestick
grafico = go.Figure(
    
    # Irá definir o conteudo do gráfico, ou seja, quais dados
    # e como serão visualizados
    data = [
        
        # Classe Candlestick que ira criar o grafico que desenha velas
        # com base nos preços de abertura, maxima, minima e fechamento
        # de um ativo ao longo do tempo.
        go.Candlestick(
            
            # Eixo x que irá receber os indices do dataset (as datas no
            # nosso caso)
            x = dados.index,
            # Ira definir os valores de abertura das ações ou ativos em
            # cada periodo de tempo.
            open = dados['Abertura'],
            
            # Ira definir os valores máximos atingidos pelos preços do ativo em cada periodo de tempo
            high = dados['Maior'],
            
            # Ira definir os valores minimos atingidos pelo preço dos
            # ativos em cada periodo de tempo
            low = dados['Menor'],
            
            # Irá definir os valores de fechamento dos ativos
            close = dados['Fechamento'],
        )
    ]
)

# Ira exibir o gráfico
grafico.show()
