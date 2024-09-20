
# Estrutura do loop For

# O loop for do python é usado para travessia sequencial, ou seja,
# é usado para iterar sobre um iteravel como atrings,tuplas, listas,
# etc. Ele se enquadra na categoria de iteração definida. Iterações
# definidas significam que o numero de repetições é especificado
# explicitamente com antecedência.

# Estrutura do for:
# for variável in objeto:
#       Loop

# No primeiro exemplo, vamos imprimir 10 valores usando do (0 ao 9)
# Como vimos anteriormente a estrutura do for é composta por 2 fatores,
# o primeiro é o nome da variável e o segundo é o objeto que será percorrido / iterado pelo for.
 
for qualquerCoisa in range(10):
    
    print(qualquerCoisa)
    
# Esse exemplo ira somar os valores com 2
for outracoisaqualquer in range(10):
    
    print("com mais 2: ",outracoisaqualquer + 2)
    

# Esse exemplo ira elevar os valores ao quadrado
for quadrado in range(10):
    
    print("Elevado ao quadrado: ", quadrado **2)
    
# Ira criar a tabuada do 3

for tabuada_3 in range(10):
    
    print("tabuada do 3: ", tabuada_3 * 3)
    

# Também é possivel passar um intervalo ao range

for intervalo in range(1, 11):
    
    print("Intervalo 1 a 10: ", intervalo)
    
# Vamos agora adicionar saltos na impressão do intervalo
# passado pro range

for saltos in range(1, 101, 5):
    
    print("1 a 100 de 5 em 5: ", saltos)


# Vamos usar o for para iterar sobre uma lista e imprimir 
# cada elemento da lista de paises

lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']

for lista_paises in lista:
    
    print("Paises da lista: ", lista_paises)
    

# Por ser uma string, podemos usar dentro do for as funções de 
# manipulações de string, como por exemplo o upper

for lista_paises_maiusculo in lista:
    
    print("Paises Maiusculos: ", lista_paises_maiusculo.upper())

# Também é possivel criar estruturas condicionais dentro do for,
# por exemplo:

for pais in lista:
    
    if pais == 'Uruguai':
        
        print("O ", pais, " é bicampeão mundial")


# Uma outra maneira interessante de acessar os elementos da lista
# é através de seu tamanho usando o comando len

for tamanho_lista in range(len(lista)):
    
    # Agora basta imprimir a lista usando como indice a variável
    # tamanho_lista que no for armazena o tamanho da lista
    print("Acesso pelo tamanho da lista: ", lista[tamanho_lista])
    


# O enumerate do for possibilita enumerar os elementos de uma lista,
# por exemplo:

# nessa estrutura a variável "indice" representa os valores da 
# numeração e a variável "Lista numerada" representa os elementos
# da lista
for indice, lista_numerada in enumerate(lista):
    
    print(indice, lista_numerada)
    


# Vamos usar o for dentro de uma lista

lista_com_for = [numeros for numeros in range(0,10,2)]

print('Lista com for: ', lista_com_for)


lista_com_for_elevado_ao_quadrado = [numeros **2 for numeros in range(0, 11)]

print("Lista com for elevado ao quadrado: ", lista_com_for_elevado_ao_quadrado)

# Vamos usar o for para adicionar elementos em uma lista numérica

lista_vazia = []

for loop in range(1, 11):
    
    # Insere dados na lista, se não me engano cada novo dado ele
    # adiciona no final da lista
    lista_vazia.append(loop)


# Agora que já inserimos dados na lista vazia, vamos imprimi-la

print("Dados da lista vazia: ", lista_vazia)