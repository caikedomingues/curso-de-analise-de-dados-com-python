

# Módulo 3: Medidas de dispersão

# Auxiliam as medidas de tendência central a descrever o conjunto de
# dados adequadamente. Indicam se os dados estão, ou não, próximos uns
# dos outros.


# Serve para criação de gráficos e carregamentos de datasets
# da própria biblioteca
import seaborn as sns

# Serve para visualizar gráficos
import matplotlib.pyplot as plt

# Ignorando as mensagens de warning
import warnings

# Função que manipula warnings, no nosso caso, vamos ignorar todos 
# os warnings
warnings.filterwarnings('ignore')



# carregando o dataset iris da biblioteca seaborn
base_dados = sns.load_dataset('iris')


# Amplitude total: é a diferença entre o maior valor e o menor valor
# do conjunto de dados observado

# Vamos calcular  amplitude total da coluna sepal_length

print("AMPLITUDE TOTAL DA COLUNA SEPAL_LENGTH")

print("Valor máximo da coluna: ", base_dados['sepal_length'].max())

print("Valor minimo da coluna: ", base_dados['sepal_length'].min())

# Variável que ira calcular a diferença entre os valores

amplitude_total = base_dados['sepal_length'].max() - base_dados['sepal_length'].min()

print("Amplitude Total: ", amplitude_total)

# Amplitude interqualitica: A amplitude interqualitica é a diferença entre o terceiro quartil (75% dos dados) e o primeiro quartil(25% dos dados). Esta medida é mais estavel que a amplitude total por não considerar os valores mais extremos.

# Primeiro vamos descrever a coluna senpal_length para descobrir a posição
# do primeiro e do terceiro quartil

print("DESCRIÇÃO DA COLUNA SEPAL_LENGTH")

# Descrição da coluna
print(base_dados['sepal_length'].describe())

# filtrando o valor do primeiro quartil
print("primeiro quartil: ", base_dados['sepal_length'].describe()[4])

# filtrando o valor do terceiro quartil
print("terceiro quartil: ", base_dados['sepal_length'].describe()[6])

# Calculo da diferença entre os quartis

amplitude_interqualitica = base_dados['sepal_length'].describe()[6] - base_dados['sepal_length'].describe()[4]

print("Amplitude Interqualitica ", amplitude_interqualitica)

# Amplitude semi-interqualitica: é definida como a média aritmética
# da diferença entre mediana e os quartis. Basicamente é a média
# aritmética do primeiro e do terceiro quartil

# Cáculo da amplitude semi-interqualitica
print("CALCULO DA AMPLITUDE SEMI-INTERQUALITICA")

# filtrando o primeiro quartil da coluna
primeiro_quartil = base_dados['sepal_length'].describe()[4]

# filtrando o terceiro quartil da coluna
terceiro_quartil = base_dados['sepal_length'].describe()[6]

# Calculo da média aritme´tica da diferença entre os quartis
amplitude_semi_interqualitica = (terceiro_quartil -  primeiro_quartil) / 2

print("amplitude semi-interqualitica: ", amplitude_semi_interqualitica)

# Variança: Medida de dispersão que mostra quão distantes os valores 
# estão da média, para calcular o valor, vamos usar a função var()

print("CÁLCULO DA VARIÂNCIA DA COLUNA SEPAL LENGTH")

print(base_dados['sepal_length'].var())

# Desvio padrão: é o resultado positivo da raiz quadrada da variância

print("DESVIO PADRÃO DA COLUNA SEPAL_LENGTH")

print(base_dados['sepal_length'].std())

# Medidas de assimetria: é um indicador da forma de distribuição de
# frequência e/ou um histograma, esta-se buscando, também, identificar
# a forma da distribuição dos dados.

# simetrica: se média = mediana = moda ou As = 0

# assimétrica negativa: se média <= mediana <= moda ou As < 0

# assimetrica positiva: se moda <= mediana <= media ou As > 0

# As: coeficientes de simetria, é uma medida que descreve a simetria
# de uma distribuição de dados.

# Função que ira calcular a assimetria da coluna sepal_length

print("CALCULO DA ASSIMETRIA DA COLUNA SEPAL_LENGTH")

print(base_dados['sepal_length'].skew())

# Vamos visualizar melhor essa assimetria (positiva no nosso caso) usando um gráfico kdeplot

# kdeplot: Representação gráfia da função de densidade de probabilidade
# de uma variável continua. Ele é uma forma suavizada do histograma
# e fornece uma estimativa da densidade de probabilidade de uma 
# variável em um determinado intervalo.

# A função recebe como parametro a base de dados com a coluna que será
# análisada
sns.kdeplot(base_dados['sepal_length'])

# Exibição do gráfico
plt.show()

# Medidas de Curtose: A medida de curtose é o grau de achatamento da 
# distribuição, é um indicador da forma de distribuição.

# leptocurtica: Quando a distribuição apresenta uma curva de frequência
# bastante fechada, com os dados fortemente concentrados em torno de seu
# centro, k < 0,263

# Mesocurtica: quando os dados estão razoavelmente concentrados em torno
# do seu centro, k = 0,263

# platicurtica: quando a distribuição apresenta uma curva de frequencia 
# mais aberta, com os dados francamente concentrados em do torno do seu
# centro k = 0,263

# Podemos calcular a curtose através da função kurtosis

print("MEDIDA CURTOSE DA COLUNA SEPAL_LENGTH")

print(base_dados['sepal_length'].kurtosis())