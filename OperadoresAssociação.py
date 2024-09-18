
# Operadores de Associação

# Os operadores de associação são usados para testar se uma sequencia
# é apresentada em um objeto
# 1. in: retorna true se uma sequencia com o valor especificado estiver
# presente no objeto.
# 2. not in: Retorna True se uma sequencia com o valor especificado 
# não estiver presente no objeto


# Para demonstrar o uso do operador vamos criar uma lista

lista_açoes = ['Ragazzo', 'via', 'carrefour']

# vamos verificar se 'via' existe na lista

print("Tem via na lista? ", 'via' in lista_açoes)

print("Não tem via na lista? ", 'via' not in lista_açoes)

# Agora vamos testar os operadores com um dado que não existe na lista

print("Tem 22 na lista? ", '22' in lista_açoes)

print("Nao tem 22 na lista? ", '22' not in lista_açoes)