

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
        # dos valores dos atributos   
        
        # Atribuição dos atributos da classe 
        self.nome = nome
        
        self.idade = idade
        