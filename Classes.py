

# Classes / Objetos 

# Python é uma linguagem de programação orientada a objetos
# Quase tudo em python é um objeto, com suas propriedades
# e métodos. Uma classe é como um construtor de objetos,
# ou um 'projeto' para criar objetos

class Pessoa:
    
    # Construtor da classe
    def __init__(self, nome, idade):
    
        # O self faz referencia ao próprio objeto
        # então o utilizamos para realizar a atribuição 
        # dos valores aos atributos   
        
        # Atribuição dos atributos da classe 
        self.nome = nome
        
        self.idade = idade
    
    
    # Método: no caso das classes, mesmo que a dua função não necessite
    # de metodos você deve passar como parametro o self que ira fazer
    # referencia aos elementos da classe dentro do seu método
    
  
    # Para exemplificar o uso de uma classe vamos fazer um breve
    # exercicio que ira verificar se o usuário é ou não menor
    # de idade.
    
    # Metodo de boas vindas que ira apresentar uma mensagem
    # de saudação ao usuário  
    def boas_vindas(self):
        
        # Como vimos anteriormente, vamos usar a referencia self
        # para acessar o nome do objeto pessoa
        print("Olá ", self.nome, " seja bem-vindo ")
    
    # Metodo que ira recusar o "acesso" do usuário
    def recusado(self):
        
        print("Seu acesso foi recusado")
    
    # Metodo que ira verificar se o usuário é maior de idade
    def Maior_idade(self):
        
        # Se o usuário for maior de idade o metodo irá chamar
        # o metodo de boas vindas e imprimir uma mensagem
        if(self.idade >= 18):
            
            print("A pessoa ", self.nome, " é maior de idade")
            
            self.boas_vindas()
        
        # Caso contrário, o sistema ira chamar o metodo de acesso
        # negado e também irá imprimir uma mensagem
        else:
            
            print("A pessoa ", self.nome, " é menor de idade" )
            
            self.recusado()



# Fora da classe/ objeto, vamos definir 2 variaveis que irá
# ler as respostas do usuário
nome = str(input("Qual o seu nome? "))

idade = int(input("Qual a sua idade? "))

# Após a leitura vamos instanciar o objeto pessoa e 
# passar como parametro as variaveis nome e idade
# (Variáveis que leram as respostas do usuário)
pessoa = Pessoa(nome, idade)

# Chamada do metodo que ira verificar a idade do usuário
pessoa.Maior_idade()