# Correlação de spearman: Uma vez que a correlação de spearman segue uma
# lógica monotônica, e não tem pressupostos lineares como na correlação
# de Pearson, é possivel utilizar o rs(relação de spearman) para relações não lineares.


# biblioteca que permite construir gráficos e carregar datasets

import seaborn as sns

# biblioteca que ira permitir a visualização dos gráficos

import matplotlib.pyplot as plt


# Carregando o dataset iris

base_dados = sns.load_dataset('iris')

# para realizar a correlação spearman, basta passar como parametro
# para o corr o valor 'spearman'.

# Antes de usar o método é necessário garantir que apenas as 
# colunas numéricas sejam selecionadas

# O metodo select_dtypes tem como objetivo filtrar os dados de acordo
# com os tipos especificados no include, que é o argumento do método
colunas_numericas = base_dados.select_dtypes(include=[float, int])

print("CORRELAÇÃO SPEARMAN")

print(colunas_numericas.corr('spearman'))


# A correlação spearman também pode ser visualizada no mapa de calor (heatmap)
# O metodo ira receber como parametro a base de dados e o annot
# como True para possibilitar que os valores numéricos apareçam no 
# mapa.
sns.heatmap(colunas_numericas.corr('spearman'), annot=True)
# Exibição do gráfico
plt.show()


# Vamos ver agora a correlação em um scatterplot (gráfico de dispersão)

sns.scatterplot(data=colunas_numericas, x='petal_length', y='petal_width')

plt.show()

