
# Tipos de informação
# text Type: str
# numeric Type: int, float, complex
# Sequence Types: lista, tupla, range
# Mapping Type: dict
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview

string = "Olá Mundo"

inteiro = 20

flutuante = 100.5

complex = complex(1j)

lista = ["Maça", "Morango"]

tupla = ('A', 'B') 

range = range(6)

dicionario = {'nome':'Ademir', 'Idade': 30}

set = set('ABC')

frozenset = frozenset('ABC')

booleano = bool(5)

variavel_bytes = bytes(5)

ByteArray = bytearray(5)

memoryview = memoryview(bytes(5))


# Vamos usar a biblioteca datetime para pegar a data atual do sistema

from datetime import datetime

data = datetime.today().date()

print(data)

# A função type tem como objetivo retornar o tipo de uma
# determinada variável
print("Tipo da variável: ", type(string))

print("Tipo da variável: ", type(inteiro))

print("Tipo da variável: ", type(dicionario))
