

# Módulo 2 - Medidas Separatrizes
# Estas medidas são valores que ocupam posições no conjunto de dados,
# em rol, dividindo-o em partes iguais e podem ser: 

# 1.Quartil: Os quartis dividem o conjunto de dados em quatro partes
# iguais

# 1°quartil: 25% dos dados são valores menores ou iguais ao valor
# do primeiro quartil

# 2° quartil: 50% dos dados são valores menores ou iguais ao valor
# do segundo quartil

# 3° quartil: 75% dos dados são valores menores ou iguais ao valor
# do terceiro quartil.

# Para criação de gráficos e carregamento dataset iris
import seaborn as sns

# para visualização dos gráficos

import matplotlib.pyplot as plt


# Carregamento do dataset iris da biblioteca seaborn

base_dados = sns.load_dataset('iris')

# Descrição da coluna 'sepal_length'

# o std é o desvio padrão da coluna

print("DESCRIÇÃO DA COLUNA SEPAL_LENGTH")

print(base_dados['sepal_length'].describe())

# Com isso podemos concluir que:

# 25% dos dados: de 4.3 até 5.1

# 50% dos dados de 5.1 até 5.8

# 75% dos dados de 5.8 até 6.4

# Também podemos visualizar essas informações de forma gráfica com o boxplot

# Criação do boxplot da coluna sepal_length
sns.boxplot(base_dados['sepal_length'])

# Exibição do gráfico
plt.show()
