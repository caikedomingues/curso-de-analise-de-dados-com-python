# Pacote Externo -Time

# Este módulo fornece várias funções relacionadas ao tempo

# import do pacote time

import time

# A primeira função que iremos utilizar é o sleep, que serve para
# adicionar pausas na execução do programa, por exemplo:

print("comecei agora.....")

time.sleep(3) # O metodo recebe como parametro a quantidade de segundos
# que a execução ira ficar pausada.
print("Terminei")

# A função localtime, tem como objetivo mostrar de forma detalhada as
# informações do horário local como: o ano, o mes, o dia, a hora, 
# os minutos, os segundos, dia da semana, se o horario de verão
# esta ou não em vigor e o dia do an0 (de 1 a 366).
agora = time.localtime()

print("Local time: ", agora)


# Também é possivel configurar o formato das instruções usando strftime

hora_formatada = time.strftime('%m/%d/%y, %H:%M:%S', agora)
 
print("Hora formatada: ", hora_formatada)

# Com o strptime, podemos extrair informações de datas em formato de
# strings 

time_texto = '21 June, 2021'
# Para a função funcionar a gente passa como parametro, na ordem que 
# está escrito no texto, o que cada parte significa (dia, mes, ano)
# Observação: no pacote time, o mes é referenciado por meio da letra B
time_texto_formatado = time.strptime(time_texto, '%d %B, %Y')

print("Time_texto: ", time_texto_formatado)

