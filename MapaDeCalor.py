# Mapa de calor

# o termo "mapa de calor" foi originalmente utilizado para identificar
# áreas com maior ou menor grau de temperatura ambiental. Serve para
# dimensionar a refrigeração, isolamento térmico e indicar o melhor 
# posicionamento de pessoas e máquinas em um ambiente. Porém, como
# o termo entrega um entendimento mais fácil dos gráficos de frio
# e calor, passou a ser utilizado também em outras áreas.

# Serve para possibilitar a manipulação e a análise dos dados
import pandas as pd

# é parte do plotly e serve para visualizar dados de maneira mais
# interativa e é projetado para facilitar a criação de gráficos
# de forma simples e rápida, com menos código necessário, oferecendo
# uma interface de alto nivel.

# Vantagens: permite criar graficos complexos com poucas linhas de código,
# todos os gráficos criados com plotly são interativos, suporta uma grande
# variedade de gráficos, funciona muito bem com dataframes pandas, oferece
# opções de personalização.
import plotly.express as px

# Para exemplificar melhor vamos criar uma lista contendo as cidades

cidades = ['Santo André','São Bernardo do Campo', 'Diadema', 'São Caetano do Sul', 'Mauá', 'Ribeirão Pires', 'Rio Grande da Serra', 'São Paulo']


# Vamos criar uma lista contendo o nome 'São Paulo' (estados das cidades listadas ácima) 8 vezes, uma para cada cidade do estado.

estado = ['São Paulo','São Paulo', 'São Paulo', 'São Paulo', 'São Paulo','São Paulo', 'São Paulo', 'São Paulo'] 

# Lista criada com as latitudes e longitudes das cidades

latitude = [-23.6666, -23.6944, -23.6226, -23.6687, -23.7141, -23.7457, -23.5489, -23.5488]

# lista criada com as longitudes das cidades.
longitude = [-46.5322, -46.5654, -46.6234, -46.5489, -46.4614,
              -46.4117, -46.4022, -46.6388]

# Lista com a quantidade de vendas em cada cidade
vendas = [100, 120, 50, 50, 70, 90, 250, 400]

# Agora, vamos criar um dicionário que irá conter as listas

dicionario = {
    
    'Cidades': cidades,
    'UF': estado, 
    'Lat': latitude,
    'Long': longitude,
    'Vendas': vendas
    
}

 
 # Transformando o dicionário em um dataframe
 # Agora os rótulos do dicionário se tornarão as colunas
 # do dataframe e as listas serão as linhas.
base_dados = pd.DataFrame(dicionario)


print("5 PRIMEIRAS LINHAS DO DATAFRAME")

print(base_dados.head())

# Criação do mapa de calor

# Variável que ira receber como valor a função density_mapbox,
# que serve para criar os mapas de calor
mapa_de_calor = px.density_mapbox(
    
    # A função irá receber como parametro:
    
    # A base de dados analisada
    base_dados, 
    # A latitude que recebera como valor os valores da coluna latitude
    lat = 'Lat',
    # A longitude que receberá como valor os valores da coluna longitude
    lon = 'Long',
    # O parametro z que ira receber a coluna de vendas
    # Esse parametro serve para representar a intensidade ou o
    # valor numérico que será utilizado para criar o mapa de calor
    # Esse parametro determina como os pontos do mapa serão analisados
    # para calcular a densidade em cada área.
    z='Vendas',
    # Define o raio de influencia dos pontos no mapa de calor
    radius = 30,
    # Centro inicial do mapa, ajustado para latitude e longitude 
    # especificos
    center = dict(lat=-23.700, lon=-46.5555),
    
    # Nivel de zoom inicial
    zoom = 7,
    # Estilo do mapa
    # Observação: esse estilo não necessita da chave de acesso do site
    # mapbox
    mapbox_style = 'open-street-map'
)

# Exibição do gráfico de calor
mapa_de_calor.show()


