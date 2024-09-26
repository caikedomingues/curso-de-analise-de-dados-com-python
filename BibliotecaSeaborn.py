

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