

# Comando Round

# Quando trabalhamos com numeros flutuantes, podemos arredontar
# (diminuir a quantidade de casas decimais pra ser mais exato)
# o valor usando um comando nativo do python, o comando 
# round(valor, numero de casas)


#Criando um exemplo

valor_exemplo = 12.124367878

# Agora, vamos arredontar o valor usando o comando round que 
# irá receber 2 parametros: o valor que será arredontado e 
# numero de casas decimais

valor_arredontado = round(valor_exemplo, 2)

print("Valor arredontado: ",valor_arredontado)