# Módulo 4- Correlação 

# Quando fazer análise de coorrelação?

# Quando você tem uma hipótese de que o aumento ou queda de uma variável
# estão associados a evolução de outra variável, por exemplo, se aumentar
# o desconto, as vendas também aumentam

# Correlação de Pearson: O coeficiente de correlação de Pearson pode
# ter um intervalo de valores de +1 a -1. Um valor de 0 indica que não
# há associação entre as duas variáveis. Um valor maior que 0 indica
# uma associação positiva. Isto é, á medida que o valor de uma variável
# aumenta, o mesmo acontece com o valor da outra variável. Um valor menor
# que 0 indica uma associação negativa. Isto é, á medida que o valor de
# uma variável aumenta, o valor da outra diminui.


# Ira permitir carregar o dataset iris e criar gráficos

import seaborn as sns

# Ira permitir visualizar os graficos

import matplotlib.pyplot as plt


# Carregando o dataset iris da biblioteca seaborn

base_dados = sns.load_dataset('iris')

# Após carregar o dataset, vamos chamar o metodo corr que ira calcular 
# a correlação entre as variáveis

print("CORRELAÇÃO")

# Antes de chamar o metodo é necessário garantir que as colunas análisadas, sejam de tipos numéricos como float e int, para isso
# vamos usar a função select_dtypes que tem como objetivo selecionar
# as colunas de um datafrane com base em um tipo de dados. A função
# recebe como argumento o include que ira conter os tipos de dados
# que queremos filtrar
colunas_numericas = base_dados.select_dtypes(include=[float, int])

# Função que ira calcular a correlação entre as variáveis
print(colunas_numericas.corr())


# Também podemos visualizar essas informações em um mapa de calor
# Observação: Quanto mais próximo de 1, maior é a correlação entre
# as variáveis 

# A função heatmap recebe como parametro a base de dados com o metodo corr (que calcula a correlação) e o annot que ira definir se os valores
# numéricos irão ou não aparecer no gráfico de calor
sns.heatmap(colunas_numericas.corr(), annot=True)
# Exibição do grafico
plt.show()


# Outra maneira de visualizar correlaçoes é através de scatterplots
sns.scatterplot(data=base_dados, x='petal_length', y='petal_width')

plt.show()