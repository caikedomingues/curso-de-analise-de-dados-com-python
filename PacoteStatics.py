

# Pacote statics

# Este módulo fornece funções para calcular estatisticas
# matemáticas de dados numéricos e interage com as listas

import statistics

lista = [12, 15, 28, 31, 56, 78, 80, 12]


# Funçaõ que calcula a média dos valores

print("Média dos valores da lista: ",statistics.mean(lista))

# função para calcular a mediana (valor que esta no centro de um conjunto de valores)

# Observação: se o numero central não existir, ele ira tirar
# a media entre os 2 valores mais próximos do centro
print("Mediana da lista: ", statistics.median(lista))

# Função que calcula a moda(valor que mais aparece em um conjunto numérico) de um conjunto de valores
print("Moda da lista: ", statistics.mode(lista))

