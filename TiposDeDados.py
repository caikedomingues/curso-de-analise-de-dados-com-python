



# Tipos de dados
# 1 - Listas: são criadas usando [] (chaves)
# 2 - Tuplas: São criadas usando () (parenteses)
# 3 - Dicionários: são criados usando {} (cochetes)
# Esses tipos de dados podem receber qualquer tipo de
# informação, inclusive operações aritméticas.

#listas: servem para armazenar uma cadeia de valores
lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8 , 9]

# Como não é possivel concatenar listas, eu converti os
# valores para string
print("Lista de valores " + str(lista_exemplo))

lista_exemplo_2 = ['nome', 'sobrenome', 'idade', 4, 5]

print(lista_exemplo_2)

# Também é possivel criar uma lista dentro de uma outra lista
lista_exemplo_3 = [1, 'texto', True, [1,2,3]]

print(lista_exemplo_3)


# Tuplas: são cadeias de valores de qualquer tipo que são imutaveis, ou seja, ao criar uma tupla, você não pode alterar os valores dela.

tupla_exemplo_1 = (1, 2, 3, 4, 5, 6)

tupla_exemplo_2 = ('texto', True, 2, 2.90)

print(tupla_exemplo_1)

print(tupla_exemplo_2)

#Dicionários: são organizados por chaves e valores, ou seja, é 
# necessário que cada valor tenha uma chave

dicionario = {
    
    #chave   #valor
    'index': 'valor',
    'id' : 1,
    'nome': 'cassio',
    'Lista' : lista_exemplo,
    'Tupla' : tupla_exemplo_1
    
    # Também é possivel criar listas e tuplas dentro de um dicionário
}

print(dicionario)
