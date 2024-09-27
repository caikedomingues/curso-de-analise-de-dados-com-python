

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