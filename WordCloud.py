

# Word Cloud
# As word Clouds (também conhecidas como wordie, word college ou tag cloud)
# são representações de várias palavras que dão maior destaque as palavras
# que aparecem com mais frequência. No caso das Mentimeter Word Cloud, as
# palavras adicionadas com mais frequencia pelos membros da audiência através de seus smartphones.
# Esse tipo de visualização ajuda apresentadores a coletar informações
# de uma maneira que todos possam entender

# Biblioteca que permite realizar operações em arrays

import numpy as np

# Permite manipular/analisar dados
import pandas as pd

# Permite visualizar os dados 
import matplotlib.pyplot as plt

# A biblioteca é usada para gerar nuvens de palavras que são representações visuais de texto onde a frequencia de cada 
# palavra está relacionada ao tamanho da sua imagem. Palavras
# mais frequentes aparecem maiores, enquanto as menos frequentes
# aparecem menores. Essa biblioteca é util para visualizar a relevancia
# ou a frequencia de termos em um conjunto de dados de texto, como
# artigos, livros, redes scoiais, etc.

from wordcloud import WordCloud

texto = "A análise de dados com Python permite extrair informações valiosas de grandes volumes de dados. Ferramentas como pandas, seaborn e wordcloud tornam o processo mais simples e eficiente, facilitando a visualização e compreensão de padrões e tendências."

# Criação da nuvem de palvras

# Wordcloud: classe que ira gerar nuvens de palavras e recebe como argumento, comandos que irão formatar a aparição da nuvem
nuvem_palavras = WordCloud(
    
    # Ira definir a cor de fundo da nuvem
    background_color='black',
    
    # Ira definir a largura da nuvem
    width=100,
    
    # Ira definir a altura da nuvem
    height=600
).generate(texto)


# Visualização da nuvem
# Ira configurar o tamanho da imagem
fig, ax = plt.subplots(figsize=(10,7))
# Usado para exibir imagens em um gráfico, o argumento é o 
# conjunto de palavras e o interpolation define a forma como
# a imagem é interpolada ou suavizada ao ser exibida.
plt.imshow(nuvem_palavras, interpolation='bilinear')
# Retira os eixos x e y
plt.axis("off")

# exibição do gráfico
plt.show()

