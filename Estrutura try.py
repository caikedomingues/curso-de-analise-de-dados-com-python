
# Estrutura try

# O try permite testar um bloco de código quanto a erros
# O except permite que você lide com erros
# O else permite executar código quando não há erros
# O finally permite que você execute códigos, indepentemente
# do resultado dos blocos try e except.

try:
    
    0 / 0

except: 
    
    print('Não deu certo')

finally:
    
    print('Programa encerrado')



try:
    
    1 / 1
    
    print('Deu certo')

except:
    
    print('Não deu certo')
    
finally:
    
    print('´Programa encerrado')