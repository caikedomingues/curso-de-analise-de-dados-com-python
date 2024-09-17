
# Fatiamento de strings

# String são listas de bytes representando caracteres
# Podemos acessar suas posições usando colchetes
# string [posição inicial, posição final]


minha_string = "Aprender python é top!"

# Como strings são listas de bytes, é possivel acessarmos 
# caracteres através de seus indices

# Vamos acessar a primeia letra da string
print(minha_string[0])

# caso você passe como parametro numeros negativos, o sistema vai inverter a ordem 

# Vamos mostrar a ultima letra da string
print(minha_string[-1])

# Vamos mostrar a segunda letra da string
print(minha_string[-10])

# Também é possivel criar um intervalo, por exemplo,
# podemos imprimir a partir da segunda letra da string
print(minha_string[-10:])

# Outro exemplo de intervalo, vamos pegar da posição 0 até
# a posição 10
print(minha_string[0:10])