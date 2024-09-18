


# Operadores de identidade
# Os operadores de identidade são usados para comparar os objetos
# não se forem iguais, mas se forem realmente o mesmo objeto(tipo),
# com a mesma localização de memoria

# is: retorna True se ambas variáveis forem o mesmo objeto
# is not: True se ambas as variáveis não forem o mesmo objeto

string_01 = "Ola Mundo"

string_02 = "Olá pessoas"

print("São iguais? ", type(string_01) is type(string_02))


print("São diferentes? ", type(string_01) is not type(string_02))