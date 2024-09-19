
# Pacote datetime

# O datetime módulo fornece classes para manipulação de datas e horas

# Import do pacote que contém vários metodos de manipulaçãon de datas

import datetime

# A primeira função que iremos utilizar serve para pegar o dia atual
# do sistema
dia_hoje = datetime.datetime.today()

print("Data: ",dia_hoje)

# Verificação do tipo do dado que ira retornar que a variável é do
# tipo datetime, ou seja,  do formato data
print("Tipo do dado: ", type(dia_hoje))

# Também é possivel mostrar só a data do sistema se utilizarmos a função
# date da biblioteca.

data_hoje = datetime.datetime.today().date()

print("Data de hoje: ", data_hoje)

# Com a função date, podemos filtrar as informações que queremos extrair das datas

ano = data_hoje.year # Ira mostrar o ano

mes = data_hoje.month # ira mostra o mes

dia = data_hoje.day # Ira mostrar o dia

print("Ano: ", ano)
print("Mes: ", mes)
print("dia: ", dia)

print(dia,"/",mes,"/",ano)
 
 # Também é possivel criar datas usando a função date, para isso
 # basta passar ano, mes e dia como parametros da função
 
data_antiga = datetime.date(2022, 2, 1)

print("Data antiga: ", data_antiga)

# Também é possivel realizar operações aritmeticas com datas

operacao_com_datas = data_hoje - data_antiga

print("Resultado da operação: ", operacao_com_datas)

# Podemos ajustar o formato da data usando a função
# strftime que ira receber como parametro a ordem
# que queremos exibir o dia o mes e o ano da data

# para funcionar é necessário atribuir a função em 
# uma variável
data_formatada = data_hoje.strftime('%d/%m/%y')

print("Data no formato brasileiro: ", data_formatada)

# Outra maneira de realizar operações com data é utilizando
# a função time delta para especificar a quantidade de dias,
# meses e anos que queremos calcular, por exemplo:

time_delta = data_hoje + datetime.timedelta(days=30)



print("Usando o time delta: ", time_delta)