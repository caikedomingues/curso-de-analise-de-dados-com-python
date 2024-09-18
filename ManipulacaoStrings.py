

# Manipulação de strings

# Um tipo de dado bastante usado no dia a dia são as strings, 
# ou cadeias de caracteres (ou sequencia de caracteres). O
# tipo de dados string ou str como é chamado em python, possui
# varias operações uteis associadas a ele. Essas operações 
# tornam o python uma linguagem bastante propricia para 
# manipulações de textos. Algumas funções mais utilizadas:

# replace()

# startswith()

# endswith()

# count()

# capitalize()

# isdigit()

# isalnum()

# upper()

# lower()

# find()

# strip()

# split()


string = "Olá mundão"

# Calculo do tamanho da string

print("Tamanho da string: ", len(string))

# Replace: O comando replace tem como objetivo substituir os valores de uma string
# por exemplo, vamos substituir a palavra mundão por mundo, para isso, vamos passar para a função replace 2 parametros: o valor antigo e o novo valor

# Para a função funcionar, devemos atribuir ela em uma outra variável
nova_string = string.replace("mundão", "mundo")

print("Novo valor da variável: ", nova_string)


# startswith(): Serve para verificar se a string começa com uma
# determinda letra ou palavra

print("Começa com 'olá? '", string.startswith("Olá"))

print("Começa com 'mundão'? ", string.startswith("mundão"))

print("Começão com 'O'? ", string.startswith("O"))


#endswith: Verifica o fim de uma string

print("Termina com 'mundão'? ", string.endswith("mundão"))

print("Termina com 'Olá'? ", string.endswith("Olá"))

print("Termina com 'o'? ", string.endswith("o"))

# Count(): Serve para contar a quantidade de letras ou palavras que uma string possui

print("Quantas letras m a string possui? ", string.count("m"))


# Capitalize: Serve para adicionar letras maiusculas nas iniciais das
# palvras

nome = 'ronaldo'

print("Nome com a inicial maiuscula: ", nome.capitalize())

# isdigit: Verifica se os valores de uma string são numéricos

cpf = '123456789'
cpf2 = 'abc123'

print("é um digito? ", cpf.isdigit())

print("é um digito? ", cpf2.isdigit())

# isalnum: verifica se uma string é alfa numerica(que possui letras e numeros)

print("É alfa numerico? ", cpf2.isalnum())

print("É alfa numérico? ", string.isalnum())

# upper: Transforma todos os caracteres de uma string em maisculo

print("String em maisculo: ", string.upper())

# lower: Transforma todas as string em minusculo

palavra_maiuscula = "MELÂNCIA"

print("String em minusculo: ", palavra_maiuscula.lower())

# find: Serve para localizar a posição de uma letra ou palavra na string
frase = "Hoje está calor"

print("Posição da palavra 'calor': ", frase.find("calor"))

print("Posição da letra 'o': ", frase.find("o"))

# strip: serve para remover os espaços no inicio e no fim das strings

endereco = " R Augusta 120, SP "

print("String com o espaço: ", endereco)

print("String sem os espaços: ", endereco.strip())

# split(): Serve para quebrar/dividir strings, você pode se quiser
# passar como parametro um separador, mas caso não passe, ele ira 
# separar usando os espaços em branco (separador padrão). Resumindo
# a função split transforma a nossa string em uma lista de palavras

nome_rua = " Rua Augusta 150, centro, SP"

print("Passando como parametro um separador: ", nome_rua.split(","))

print("Sem passar um parametro(padrão): ",nome_rua.split())
