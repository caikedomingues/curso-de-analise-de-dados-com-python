

# Biblioteca do python utilizada para analise de dados com ela podemos
# realizar higienizações de dados e processos de machine learning.
# Também é possivel tratar dados com o pandas


# Import da biblioteca pandas que terá os metodos necessários
# para acessarmos o arquivo csv e tratar os dados.
import pandas as pd

# Leitura do arquivo: é necessário atribuir a uma variável, o comando de 
# acesso ao arquivo csv para podermos acessar os metodos necessários para
# a análise de dados.
df = pd.read_csv('performanceEstudantes.csv')

# função da biblioteca pandas que ira mostrar o tipo do arquivo,
# no nosso caso é um dataframe.

# DataFrame: é uma estrutura de dados em formato de tabela que armazena
# dados em formato de linhas e colunas. É parecido com uma planilha em
# excel ou uma tabela em um banco de dados.
print("TIPO DOS DADOS")
print(type(df))

# Função da biblioteca pandas que mostra as 5 primeiras linhas de cada coluna da tabela
print("5 PRIMEIRAS LINHAS DAS COLUNAS")
print(df.head())

# Função da biblioteca pandas que mostra as 5 ultimas linhas de cada coluna da tabela
print("5 ÚLTIMAS LINHAS DAS COLUNAS")
print(df.tail())

# função da biblioteca pandas que mostra a quantidade de linhas
# e colunas da tabela
# Observação: O primeiro valor é a quantidade de linhas e o segundo
# valor é a quantidade de colunas
print("QUANTIDADE DE LINHAS E COLUNAS DA TABELA")
print(df.shape)

# Metodo da biblioteca pandas que mostra as colunas da tabela
print("COLUNAS DA TABELA")
print(df.columns)

# Verifica a quantidade de linhas duplicadas na tabela, ou seja,
# é necessário a utilização da função sum que ira somar as linhas
# duplicadas da tabela
print("QUANTIDADE DE LINHAS DUPLICADAS DA TABELA")

print(df.duplicated().sum())

# Agora se utilizarmos somente a função duplicated, ela vai nos retornar
# um valor booleano em cada linhas da tabela, onde true (verdadeiro) significa que a linha é duplicada e false (falso) representa que não há linhas duplicadas.

print("LINHAS DUPLICADAS DA TABELA")

print(df.duplicated())


# função da biblioteca pandas que contém informações gerais sobre o dataframe

print("INFORMAÇÕES GERAIS DO DATAFRAME")

print(df.info())

# Verificação da quantidade de valores nulos usando o metodo sum
print("QUANTIDADE DE VALORES NULOS")

# A função isna verifica a se há ou não valores nulos na tabela
print(df.isna().sum())


# A função isna verifica se há valores nulos na tabela e retorna
# um valor booleano em cada linha da tabela
# True: contém valores nulos
# False: não contém valores nulos.
print("VERIFICAÇÃO DE VALORES NULOS NA TABELA")

print(df.isna())

# Sumário estátistico: nos passa informações como numero de
# valores de cada coluna, a média dos valores de cada coluna, o desvio padrão de cada coluna, o valor minimo de cada coluna, os quartis de cada coluna (25% dos dados, 50% dos dados(também é a média dos valores), 70% dos dados) e o valor máximo de cada coluna.
print("DESCRIÇÃO DO SUMÁRIO ESTÁTISTICO")

# A função describe do pandas nos passa o sumário estatistico das
# colunas
print(df.describe())


# Sumário estátistico de todas as variaveis (incluindo todos os tipos
# como o de textos por exemplo)

print("SUMARIO ESTATISTICO DE TODAS AS VARIAVEIS (TODOS OS TIPOS)")

print(df.describe(include='all'))

# Ira mostrar a quantidade de valores unicos em cada coluna
print("QUANTIDADE DE VALORES ÚNICOS")
print(df.nunique())

# Com o pandas posso acessar diretamente uma determinada coluna e
# aplicar nela uma função, por exemplo, vamos verificar os valores 
# nulos da coluna 'parental level of education'.

print("QUANTIDADE DE VALORES ÚNICOS DA COLUNA 'PARENTAL LEVEL OF EDUCATION'")
print(df['parental level of education'].nunique())

# A funçaõ value_counts do pandas calcula a frequencia de valores 
# das colunas

print("FREQUENCIA DE VALORES DAS COLUNAS")

print(df.value_counts())

# Agora vamos usar o value_counts em uma coluna especifica, no caso vamos
# ver a frequência entre os generos dos alunos

print("FREQUENCIA DOS VALORES DA COLUNA GENDER")
print(df.gender.value_counts())

# Agora vamos criar uma lista que conterá as colunas de pontuações
# das matérias
# lista provas

provas = ['math score', 'reading score', 'writing score']

# Agora podemos organizar / ordenar o dataset de acordo com a nossa
# lista

# Organzação do dataset de acordo com a lista de provas

# ira ordernar o dataframe com base nas colunas da lista provas
# sort_values: Função do pandas que ordena os dados com base
# nas colunas
# by: recebe como parametro as colunas que serão usadas na 
# ordenação do dataset
# ascending: Tem como obejtivo especificar se a ordenação
# deve ser crescente ou descrescente. Se fosse True, a ordenação
# seria crescente
# reset index: após ordenar os dados, os indices originais(posições das linhas) podem ficar desordenados, então, o intuito da função é reiniciar
#  o indice para começar de 0, 1, 2


# Como no vscode não há espaço suficiente, temos que usar 2 funções
# do pandas para garantir que todas as informações sejam mostradas
# corretamente

#pd.set_option('display.max_columns', None) (Ira mostrar todas as colunas)

#pd.set_option('display.max_rows', None)  (Ira mostrar todas as colunas)

# Se quiser voltar aos padrões basta digitar
# os comando: pd.set_option('display.max_columns'), pd.set_option('display.max_rows') 
print("ORGANIZAÇÃO DAS COLUNAS DE PONTUAÇÃO DAS MATÉRIAS")

print(df.sort_values(by = provas, ascending = False).reset_index(drop=True))

# Coluna com a média das provas 
# Irá calcular a média de cada coluna da tabela
print("MÉDIA DAS PROVAS")
# Esse trecho ira criar uma nova coluna
media = df['mean'] = df[provas].mean(axis=1)
# Ira mostrar todas as colunas
pd.set_option('display.max_columns', None)
print(media)

# Vamos verificar se a coluna foi criada.
print("AS 5 PRIMEIRA LINHAS INCLUINDO A NOVA COLUNA")
print(df.head())

# Outra funcionalidade do pandas é possibilitar consultas e filtros
# das informações do dataframe

# Por exemplo, vamos filtrar os alunos que: são do sexo masculino, não
# fizeram o curso de preparação para testes e possuem notas maior ou 
# igual a 70.

# Observação: casos as colunas estejam com nomes separados, devemos colocar o nome entre crases para funcionar.
print("FILTROS")
print(df.query('(gender == "male") & (`test preparation course` == "none") & (`math score`>= 70)'))



# O método loc[] é usado para selecionar linhas ou colunas de um DataFrame com base em rótulos (ou seja, condições booleanas, índices ou nomes de colunas).
print("FILTRO COM A FUNÇÃO LOC")

print(df.loc[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)])

# Agrupamentos: agrupa os dados por generos e obtem estastisticas
# descritivas

# Groupby: é usado para agrupar os dados do dataframe com base 
# nos valores de uma coluna

# provas é a lista de colunas que contém as pontuações das provas

# agg(['medan','median']): agg é o metodo que você usa para agregar
# dados, ele permite aplicar funções de agregação(como o calculo de médias, por exemplo).

print("AGRUPAMENTOS POR GENÊROS")
print(df.groupby(by='gender')[provas].agg(['mean', 'median']))

