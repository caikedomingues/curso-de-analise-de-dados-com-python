

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

# Antes de renomear, vamos eliminar possiveis espaços em branco
# que podem nos atrapalhar na renomeação das colunas

base_dados.columns = base_dados.columns.str.strip()

base_dados.rename(columns={
    'Company': 'Empresa',
    'Valuation ($B)': 'Valor ($)', 
    'Date Joined': 'Data de Adesão', 
    'Country': 'Pais',
    'City': 'Cidade',
    'Industry': 'Setor',
    'Investors': 'Investidores'
},inplace=True) # O parametro inplace=True faz com que a alteração seja aplicada diretamente no dataframe original sem a necessidade de criar
# uma cópia

# Verificando se os nomes das colunas foram modificados
print("VERIFICANDO O NOME DAS COLUNAS")
print(base_dados.columns) 

# Verificando as informações do dataframe
print("INFORMAÇÕES GERAIS DO DATAFRAME")
print(base_dados.info())

# Apesar da função info retornar a quantidade de valores nulos, podemos
# verificar quais linhas em especifico estão com os valores nulos.
# Para realizar essa ação basta usar a função isnull que irá retornar
# um valor booleano onde true indica que há valores nulos e false para
# valores não nulos.

print("LINHAS QUE CONTÉM VALORES NULOS")

print(base_dados.isnull())

# Também é possivel verificar o total de linhas nulas em cada coluna

print("TOTAL DE VALORES NULOS EM CADA COLUNA")
print(base_dados.isnull().sum())

# Excluindo os valores nulos da coluna investidores: Vamos usar a função
# dropna do pandas para excluir os 18 valores nulos da coluna investidores. Para excluir os valores nulos de uma coluna em especifico
# precisamos passar como parametro para o dropna o subset com o nome da
# coluna que deve ser afetada.
# Observação: se usarmos a função sem passarmos um parametro, iremos
# apagar os valores nulos de todas as colunas.

base_dados_sem_nulos = base_dados.dropna(subset=['Investidores'])

print("VERFICANDO SE OS VALORES NULOS FORAM APAGADOS")
# Agora vamos usar a variável base_dados_sem_nulos para podermos
# acessar as informações atualizadas do dataframe
print(base_dados_sem_nulos.isnull().sum())

# Verificando valores unicos: valores que são diferentes (não se repetem).
# Para verificar essas informações vamos usar a função nunique que retorna
# a quantidade de valores unicos de cada coluna.
print("QUANTIDADE DE VALORES UNICOS")
print(base_dados_sem_nulos.nunique())

# Verificando os valores nulos de uma coluna especifica

print("QUANTIDADE DE VALORSS ÚNICOS DA COLUNA SETOR")

print(base_dados_sem_nulos['Setor'].nunique())

# Para visualizar os valores unicos das colunas, usamos o metodo
# unique que ira mostrar os valores unicos das colunas.

print("vALORES UNICOS DAS COLUNA SETOR")

print(base_dados_sem_nulos['Setor'].unique())

# Verificando a frequência que os valores únicos aparecem 
# na coluna setor, Para realizar essa ação, vamos utilizar
# o método value_counts que tem como objetivo contar a 
# frequência dos valores únicos em uma coluna. Ela retorna
# uma Series onde os valores distintos da coluna
# são os indices e as respectivas contagens são os dados
# associados.
# Resumindo, a função ira contar quantas vezes cada valor
# unico ira aparecer em uma determinada coluna.
print("RANK DOS VALORES UNICOS DA COLUNA SETOR")

print(base_dados_sem_nulos['Setor'].value_counts())

# O value conts também permite visualizar a porcentagem da 
# frequencia do valor unico na coluna.
# Para funcionar basta passar como parametro o normalize como
# True.
print("PORCENTAGEM DA FREQUENCIA DE VALORES ÚNICOS DA COLUNA SETOR")

print(base_dados_sem_nulos.value_counts(normalize=True))


# Vamos verificar a frequencia de valores unicos em um grafico de barras
# usando a biblioteca matplotlib.pyplot.

# Define o titulo do gráfico
plt.title('PORCENTAGEM DE FREQUÊNCIA DE VALORES ÚNICOS')
# Define o tamanho da figura do gráfico(largura e altura)
plt.figure(figsize=(15,6))

# Função do matplotlib que cria gráficos de barra, a função irá
# receber como parametro: a base de dados com o metodo value_conts onde
# o index acessa os indices da série resultante, que são os valores únicos
# da coluna. O primeiro argumento são os valores do eixo x e o segundo
# argumento são os valores do eixo y.

plt.bar(base_dados_sem_nulos['Setor'].value_counts().index, base_dados_sem_nulos['Setor'].value_counts())
# Este trecho ajusta as os rótulos do eixo alterando a rotação
# para 45 graus. O argumento 'ha' define o alinhamento horizontal
# para a direita. Isso garante que, ao serem rotacionados, os rótulos não
# se sobreponham aos outros
plt.xticks(rotation=45, ha='right')
# Exibe o gráfico
plt.show()


# Verificando a frequencia de valores nulos na coluna de paises
print("FREQUENCIA DE VALORES ÚNICOS DA COLUNA DE PAISES")
print(base_dados_sem_nulos['Pais'].value_counts())

# verificando a porcentagem da frequencia de valores da coluna
# pais, dessa vez vamos multiplicar os valores por 100 para a
# visualização das porcentagens ser mais claras

print("PORCENTAGEM DA FREQUENCIA DE VALORES UNICOS DA COLUNA PAIS")
porcentagem_frequencia_pais = base_dados_sem_nulos['Pais'].value_counts(normalize=True) * 100

print(porcentagem_frequencia_pais)

# Construindo um gráfico de pizza com os valores da porcentagem de frequencia da coluna pais. Vamos usar a biblioteca matplotlib

# Ira criar o titulo do gráfico
plt.title("FREQUÊNCIA DE VALORES ÚNICOS DA TABELA PAIS")
# Irá definir o tamanho da figura
plt.figure(figsize=(22, 6))

# Função que ira criar o gráfico de pizza
plt.pie(
    
    # Base de dados analisada
    porcentagem_frequencia_pais,
    # Indice dos paises como rótulos
    labels = porcentagem_frequencia_pais.index,
    # Distancia entre o nome dos rótulos e o centro do gráfico
    labeldistance = 1.1,
    # No nosso caso não haverá sombra
    shadow = False,
    # Ângulo em que o gráfico começa a ser desenhado
    startangle = 90,
    # Formatação dos valores do gráfico
    autopct = '%1.1f%%'
)

# Exibição do gráfico
plt.show()


# Analise da frequência de valores unicos dos 10 primeiros paises.
# A análise será feita com um grafico de pizzas
# Titulo do gráfico
plt.title("ANÁLISE DE FREQUÊNCIA DOS 10 PRIMEIROS PAISES DA COLUNA")

# Tamanho da figura do gráfico (largura e altura)
plt.figure(figsize=(15,6))

# Função da biblioteca matplotlib que cria gráficos de pizza
plt.pie(
    
    # base de dados analisadas que ira conter apenas as 10 primeiras
    # linhas do  gráfico de pizza
    porcentagem_frequencia_pais.head(10),
    
    # O rótulo ira receber o indice das 10 primeiras linhas da coluna
    labels = porcentagem_frequencia_pais.head(10).index,
    
    # Distância entre o nome dos rótulos e o centro do gráfico
    labeldistance= 1.1,
    
    # Ângulo em que o gráfico será desenhado
    startangle=90,
    
    # Formatação dos valores (porcentagens do gráfico)
    autopct='%1.1f%%'
)

# Exibição do gráfico
plt.show()


# Agora vamos converter os valores da coluna 'Data de Adesão' para
# o tipo date.
# Observação nesse momento elas estão no tipo object (string/texto)

base_dados_sem_nulos['Data de Adesão'] = pd.to_datetime(base_dados_sem_nulos['Data de Adesão'])

# Verificando se a conversão foi realizada

print("VERIFICANDO SE A CONVERSÃO FOI REALIZADA COM SUCESSSO")

# A função dtypes irá mostrar o tipo de uma coluna
print(base_dados_sem_nulos['Data de Adesão'].info())

# Agora que onvertamos os valores vamos criar uma coluna para
# conter os valores mes e ano

# Criação das colunas mes e ano, onde datetimeIndex converte os dados
# da coluna 'Data de Adesão'  para um tipo de dado que facilita a 
# manipulação de informações de data. Isso é importante porque
# transforma cada valor da coluna em um objeto de data que o pandas
# pode analisar.
# Month: Ira extrair o mes da coluna 'Data de Adesão'
# Year: Irá extrair o ano da coluna 'Data de Adesão'
base_dados_sem_nulos['Mes'] = pd.DatetimeIndex(base_dados_sem_nulos['Data de Adesão']).month

base_dados_sem_nulos['Ano'] = pd.DatetimeIndex(base_dados_sem_nulos['Data de Adesão']).year

# Verificando se a coluna foi criada

print("VERIFICANDO SE AS COLUNAS FORAM CRIADAS")

print(base_dados_sem_nulos.head())

# Vamos agrupar os valores em pais, ano, mes
print("AGRUPAMENTO DOS VALORES")

# Para realizar o agrupamento vamos usar o metodo groupby
# que ira receber como parametro o by, uma lista das colunas
# que irão fazer parte do grupo. O count serve para contar os 
# valores não nulos de cada coluna do grupo.
print(base_dados_sem_nulos.groupby(by=['Pais', 'Ano','Mes']).count())

# Agora vamos agrupar os valores do pais Brazil

print("AGRUPAMENTO DOS VALORES DO BRASIL")

# Vamos usar a função loc para filtrar os registros do Brasil na base de dados.
# A função irá comparar a coluna 'Pais' e retornará uma série booleana,
# onde True significa que o valor é igual a 'Brazil' e False significa que o valor é diferente.
# Em seguida, loc utilizará essa série para selecionar as linhas onde o valor é True.
analise_agrupada = base_dados_sem_nulos.loc[base_dados_sem_nulos['Pais'] == 'Brazil']
print(analise_agrupada)

# Transformando a coluna valor em tipo numerico
# Para evitar erros, será necessário substituir os simbolos de sifrão
# por um espaço em branco/vázio.
# Para isso vamos atribuir a coluna valor o atributo str(que irá permitir operações com strings em toda a coluna valor) com o metodo replace que ira receber como parametro a string que será substituida
# e a nova string que será incluida nas colunas. O parametro regex = False ira garnatir que a função trate o sifrão($) como uma string
# e não como um metacaractere.
base_dados_sem_nulos['Valor ($)'] = base_dados_sem_nulos['Valor ($)'].str.replace('$', '', regex=False)

# Transformando a coluna valor em um tipo numérico
base_dados_sem_nulos['Valor ($)'] = pd.to_numeric(base_dados_sem_nulos['Valor ($)'])

# Verificando se a conversão deu certo
print("VERIFICANDO SE A MUDANÇA DE TIPO FOI REALIZADA COM SUCESSO")

# Imprimindo as informações gerais da coluna valor.
print(base_dados_sem_nulos['Valor ($)'].info())

# Vamos analisar o valor que cada pais arrecada em um determinado setor
# para isso, vamos agrupar as colunas por paises e setores e iremos
# somar o valor arrecado de cada um em seus devidos setores.
print("AGRUPAMENTO POR PAIS E SETOR")

# O metodo groupby irá agrupar os dados do dataframe pelas colunas
# pais e setor. O metodo groupby permite que você agrupe os dados
# com base nos valores dessas colunas, criando grupos distintos
# de linhas com base nas combinaçoes únicas dos valores das colunas.
# A coluna valor é a coluna que queremos somar os valores, com o 
# objetivo de verificar o total de valor arrecado pelos paises
# em seus setores.
# O método sum irá somar os valores da coluna 'Valor ($)'.
# O método reset_index irá redefinir os índices, transformando
# os índices gerados pelo agrupamento em colunas normais no DataFrame,
# garantindo que o resultado tenha um índice padrão numérico.
# Resumindo o reset_index ira criar uma coluna que ira dar indices/
# posições para os valores das colunas pertencentes ao grupo
print(base_dados_sem_nulos.groupby(by=['Pais', 'Setor'])['Valor ($)'].sum().reset_index())

# Podemos ordenar os valores em forma decrescente usando o sort_values
print("ORDENANDO OS VALORES DO AGRUPAMENTO")

# Esse trecho ira agrupar os valores por paises e setores e ira calcular
# o total do valor arrecado por cada pais.
# O reset_index ira transformar os indices gerados pelo agrupamento
# em colunas normais.
# o sort_values ira ordenar os valores em forma decrescente (Do maior
# para o menor), sendo assim, ele receberá como parametro a coluna valor
# que será o critério da organização e o ascending=False ira definir
# a ordem em que os dados serão organizados, no caso de forma decrescente
print(base_dados_sem_nulos.groupby(by=['Pais','Setor'])['Valor ($)'].sum().reset_index().sort_values(['Valor ($)'], ascending=False))


# Vamos visualizar essas informações de forma gráfica(gráfico de linhas)
# Para facilitar a plotagem, vamos atribuir o trecho anterior
# em uma variável.
analise_valor = base_dados_sem_nulos.groupby(by=['Pais', 'Setor'])['Valor ($)'].sum().reset_index().sort_values(['Valor ($)'], ascending = False)

# Titulo do gráfico
plt.title("ANÁLISE DO VALOR ARRECADADO POR CADA PAIS")
# Ira definir o tamanho da figura do gráfico
plt.figure(figsize=(15,6))
# Função da biblioteca matplotlib que irá criar um gráfico de linhas
# A função ira receber como parametro a coluna['pais'](eixo x que fica na horizontal)
# e a coluna 'Valor'(eixo y que fica na vertical)
plt.plot(analise_valor['Pais'], analise_valor['Valor ($)'])
# Irá definir a rotação e o alinhamento dos eixos x(horiontal)
plt.xticks(rotation=45, ha='right')
# Exibição do gráfico.
plt.show()