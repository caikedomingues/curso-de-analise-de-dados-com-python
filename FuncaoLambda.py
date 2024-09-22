

# Estrutura Lambda

# Uma função lambda é uma pequena função anônima. Uma função lambda
# pode receber qualquer número de argumentos, mas pode ter apenas
# uma expressão.


# Exemplos da função lambda
funcao_soma = lambda valor : valor + 10

print("Resultado da função soma 1: ",funcao_soma(1))


funcao_soma_2 = lambda valor1, valor2 : valor1 + valor2

print("Resultado da função soma 2: ", funcao_soma_2(3,3))

exemplo = lambda valor: 'verdadeiro' if valor % 2 == 0 else 'False'

print("É par? ",exemplo(4))

print("É par? ", exemplo(5))
