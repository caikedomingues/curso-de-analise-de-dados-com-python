
# Pacote Math

# O python possui um conjunto de funções matemáticas integradas, incluindo um externo módulo matemático, que permite realizar
# tarefas matemáticas em números.

import math

# criação da tupla
tupla = (10, 5, 20, 30, 40)

# O primeiro metodo retorna o valor minimo de uma sequencia numérica
print("Valor minimo da Tupla: ", min(tupla))

# Ira retornar o valor máximo de uma sequencia de numeros
print("Valor máximo de uma sequencia de numeros: ", max(tupla))

# A função abs tem como função converter valores negativos para valores
# positivos

valor_negativo = -7.25

print("Valor negativo: ", valor_negativo)

print("Valor posiivo: ", abs(valor_negativo))

# A função pow tem como objetivo realizar exponenciação, a função
# ira receber 2 parametros o valor que será elevado e o expoente

# por exemplo vamos fazer 3 elevado a 4

print("Exponenciação: ", pow(3, 4))

# O sqrt tem como objetivo retornar a raiz quadrada de um valor

print("Raiz quadrada de 81: ", math.sqrt(81))

# O metodo ceil arredonta um valor pra cima até o numero inteiro
# mais proximo

print("Numero inteiro mais proximo: ", math.ceil(1.4))

# o metodo floor arredonta um valor para baixo até o seu numero inteiro mais próximo

print("Núemro inteiro mais próximo: ", math.floor(1.4))

print("Valor de pi: ", math.pi)