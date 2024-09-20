
# Estrutura de funções

# Uma função é um bloco de código que só é executado quando é
# chamado. você pode passar dados, conhecidos como parametros,
# para uma função. Uma função pode retornar dados como resultado.

 
def boas_vindas():
     
     print("Boas vindas")
    

boas_vindas()


# função que ira somar 2 numeros: para funcionar vamos criar
# uma função que deverá receber 2 parâmetros,

def somar(valor_1, valor_2):
    
    soma = valor_1 + valor_2
    
    print("Soma dos resultados: ", soma)


# Chamada da função

somar(2,2)

# Vamos atribuir parametros a função de soma usando o for e o random

for loop in range(0,10):
    
    import random
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    
    somar(x, y)
    