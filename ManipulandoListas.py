

# Manipulando Listas

# As listas são usadas para armazenar vários itens em uma única variável.
# As listas são um dos 4 tipos de dados internos do python usados para
# armazenar coleções de dados, os outros 3 são tuplas, set e dicionarios,
# todos com qualidades e usos diferentes

# Comandos mais utilizados

# 1.append: para adicionar um item ao final da lista
# 2.len: calcular o tamanho da lista 
# 3.[]: acessar posições
# 4.del: excluir um elemento
# 5.clear: limpar a lista
# 6.insert: para inserir um item da lista em um indice especificado
# 7.extend: anexa elementos de outra lista a lista atual
# 8.remove: Remove o item especificado
# 9.pop: Remove o indice especificado
# 10.sort: Ordena os valores 
# 11.copy: faz uma cópia da lista
# 12.index: Retorna o index do elemento da lista 


# lista vazia 
lista_vazia = []

# vamos inserir valores na lista usando o comando append

lista_vazia.append(1)

lista_vazia.append(2)

lista_vazia.append(3)

lista_vazia.append("Valor")

print(lista_vazia)

# tamnho da lista

print("Tamanho da lista: ", len(lista_vazia))

print("Primeira posição da lista: ", lista_vazia[0])

# limpando a lista com o clean

lista_vazia.clear()

print("Lista vazia: ", lista_vazia)


# inserindo valores em posições especificas.

lista_vazia = [1 ,2, 3, "Valor"]

# a função deve receber 2 parametros: a posição(indice) e o dado
lista_vazia.insert(3, "zero")

lista_vazia.insert(4, 2.5)

print("Lista com insert: ", lista_vazia)

# Inserindo itens de outra lista na lista atual

# Para adicionar itens de uma lista dentro de outra, devemos utilizar
# a função extende que recebe como parametro a lista que contém os valores que serão adicionados na outra lista

lista_01 = [1, 2, 3]

lista_02 = [4, 5, 6]

# No exemplo, vamos adicionar os valores da lista 2 na lista 1

lista_01.extend(lista_02)

print("Lista 1 exetendida: ", lista_01)

# Podemos excluir/remover itens de uma lista indicando o valor que
# queremos eliminar.

# No exemplo, vamos eliminar o valor 5 da lista 1
lista_01.remove(5)

print("Lista 1 sem o valor do indice 5: ", lista_01)

# Também podemos eliminar indicando a posição do valor usando o pop

lista_01.pop(0)

print("Exclusão do valor do indice 0: ", lista_01)

# Podemos usar o sort para ordenar os valores da lista

lista_ABC = ['z', 'c', 'f', 'b','a']

# Agora ele ira organizar a lista em ordem alfabética
lista_ABC.sort()

print("Lista ordenada: ", lista_ABC)

# Também é possivel ordenar de forma invertida do Z ao A, para isso
# basta como parametro o reverse: true

lista_ABC.sort(reverse=True)

print("Lista ordenada com o sort reverse: ", lista_ABC)

# Agora vamos copiar os valores da lista e adicionar em uma nova lista

lista_nova = lista_ABC.copy()

print("Cópia da lista ABC: ", lista_nova)

# Com o metodo index você pode descobrir a posição
# de um determinado valor

print("Posição da letra c na lista: ", lista_ABC.index("c"))