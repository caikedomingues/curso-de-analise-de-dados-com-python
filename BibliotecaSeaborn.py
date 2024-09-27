

# Seaborn

# O seaborn é uma biblioteca de visualização de dados do python baseado 
# no matplotlib. Ele provê uma interface de alto nivel para a construção
# de gráficos estatisticos atrativos e informativos.


# Biblioteca utilizada para operações matematicas e operações de arrays
import numpy as np

# Importa a biblioteca pandas que é usada para análise e manipulação
# de dados
import pandas as pd

# biblioteca de visualização de dados
import seaborn as sns

# Será usado para exibir os gráfcos
import matplotlib.pyplot as plt

# Definindo um tema no seaborn
# Configura o tema padrão dos gráficos do seaborn
sns.set_theme(style='darkgrid')

# Carrega um dataset de exemplo chamado tips(gorjetas) que esta disponivel
# na biblioteca seaborn. O dataset tips contém informações sobre gorjetas
# recebidas em um restaurante. Ele possui as seguintes colunas:
# total_bill: O valor total da conta
# tip: a gorjeta dada
# sex: Gênero da pessoa que deu a gorjeta
# smoker: Se a pessoa era fumante ou não
# day: O dia da semana
# time: Se foi durante o almoço ou jantar
# size: o tamanho do grupo de pessoas na mesa.
base_dados = sns.load_dataset('tips')

# Verificando os dados do dataset
# Exibindo as 5 primeiras linhas de cada coluna
print("VERIFICANDO OS DADOS DO DATASET")
print(base_dados.head())

# Pra ficar mais fácil, vamos renomear as colunas do dataset usando a
# função rename do pandas, que possibilita renomear os nomes das colunas
# do dataset

base_dados.rename(columns={
    
    'total_bill':'Total_Conta',
    'tip': 'Gorjeta',
    'sex': 'Sexo',
    'smoker': 'Fumante',
    'day': 'Dia_Semana',
    'time': 'Periodo'
    
}, inplace=True) # O inplace modifica o dataframe origial diretamente

# Após renomear as colunas, vamos verificar se as alterações estão corretas
print("COLUNAS RENOMEADAS")

print(base_dados.head())



# Gráfico relplot: é uma função projetada para visualizar a relação
# entre duas ou mais variáveis em um conjunto de dados. Exemplos de
# utilização do relplot:
# Visualização de relações: para visualizar a relação entre 2 variáveis continuas. é particularmente útil para identificar tendencias, padrões e
# agrupamentos em dados.

# Tipo de Gráfico: por padrão, o relplot cria um gráfico de dispersão.
# No entanto, você também pode configurar para gerar gráficos de linha,
# dependendo do tipo dos dados.

# Facetas: o relplot permite que você crie multiplos subgráficos

# A função relplot recebe como argumentos os valores do eixo x, os valores
# do eixo y e a base de dados que será utilizada na criação dos gráficos 
sns.relplot(x='Total_Conta', y='Gorjeta',data= base_dados)

# Exibição do gráfico
plt.show()

# Passando outro parametro como classe no gráfico
# O hue separa os dados em categorias, no caso, vamos separar os dados
# por sexo.
sns.relplot(x = 'Total_Conta', y='Gorjeta', data=base_dados, hue='Sexo')

# Exibe o gráfico
plt.show()

# é possivel escolher no relplot o tipo do gráfico que será gerado
# através do parametro kind da função

sns.relplot(x='Total_Conta', y='Gorjeta', data=base_dados, kind='line')

# Exibição do gráfico
plt.show()

# Nessa parte, vamos criar um gráfico de linhas mostrando a relação 
# do valor da conta com a gorjeta. Nesse gráfico vamos separar os dados
# em duas categorias: fumantes e não fumantes

sns.relplot(x='Total_Conta', y='Gorjeta', data=base_dados, hue='Fumante', kind='line')

plt.show()

# Hisplot: Função utilizada para criar histogramas, que são gráficos que
# mostram a distribuição de um conjunto de dados. Em análise de dados, ele é util para visualizar como os dados estão distribuidos ao longo de intervalos ou bins, o que pode ajudar a identificar padrões como assimetria,
# outliers ou a forma geral da distribuição(normal, uniforme, etc)

# Distribuição de dados: Mostra como os dados estão distribuidos, permitindo
# visualizar frequências e identificar padrões, como uma distribuição normal
# ou enviesada.

# A função recebe como parametro a base de dados e o eixo 
sns.histplot(data=base_dados, x='Total_Conta')

# Exibição do gráfico
plt.show()


# Nos histplot também é possivel separar os dados por categoria utilizando 
# o hue

sns.histplot(data=base_dados, x='Total_Conta', hue='Fumante')

# Exibição do gráfico
plt.show()


# Barplot: é utilizado para criar graficos de barras que são uteis
# para visualizar comparações entre variáveis numericas e categóricas
# mostrando as médias ou outros estimadores 

# No exemplo, vamos comparar o total das contas entre homens e mulheres
# fumantes e não fumantes

# A função ira receber como parametro a base de dados, o eixo x, o eixo y e o hue que ira separar a categoria dos dados
sns.barplot(data=base_dados, x='Sexo', y='Total_Conta', hue='Fumante')

# Exibição do gráfico
plt.show()


# parlplot: Serve para gerar gráficos de dispersão(scatter plots) entre
# todas as combinações possiveis de variáveis numericas em conjunto de dados
# e também inclui histogramas ou (KDES) das distribuições individuais de cada variável.
# Ele é muito util na analise de dados exploratórias para identificar padrões, correlações e relações entre as variáveis.

# A função recebe como parametro apenas a base de dados que será
# análisada.

# Observação: se a sua base de dados for muito grande, ele exigira
# muita capacidade de memória pra ser processada
sns.pairplot(base_dados)

# Exibição do gráfico
plt.show()


# no pairplot é possivel separar por categorias usando o hue

sns.pairplot(base_dados, hue='Sexo')
# Exibição do gráfico
plt.show()

# No pairplot é possivel utilizar o kind para escolher o tipo de gráfico
# de correlação que será utilizado

# kde: É uma técnica de estatistica usada para estimar a distribuição de
# uma varoável continua com base em uma amostra de dados. Em vez de de exibir a frequência exata de observações, o kde cria uma curva suavizada
# que representa a probabilidade de valores diferentes

# Variável contnua: variável que pode assumir qualquer valor dentro de
# um intervalo. Em outras palavras, ela pode ter uma infinidade de 
# valores possiveis, incluindo números decimais

sns.pairplot(base_dados, kind='kde')
# Exibição de gráfico
plt.show()

# Boxplot
sns.boxplot(base_dados, x = 'Dia_Semana', y = 'Total_Conta')
# Exibição do gráfico
plt.show()

# Boxlplot com hue para separar por categorias

sns.boxplot(base_dados, x='Dia_Semana', y='Total_Conta', hue='Sexo')

# Exibição do gráfico
plt.show()