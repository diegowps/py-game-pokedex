# Tópico Python: Módulos e Importação
# Estamos importando as classes que definimos no nosso módulo
#  'criaturas'.
# Isso permite usar os "moldes" que criamos para construir os
#  objetos.
from criaturas import CriaturaFogo, CriaturaAgua

# Tópico Python: Instanciação de Objetos
# Aqui estamos criando as criaturas de verdade. Cada linha cria
#  um novo objeto
# na memória, chamando o método __init__ da classe correspondente.
# Nota: As imagens não precisam existir neste momento. 
# Estamos apenas guardando o caminho.
dragao_chama = CriaturaFogo(
    nome="Dragnir", 
    hp=150, 
    ataque=25, 
    imagem_path="imagens/dragao.png"
)

salamandra_infernal = CriaturaFogo(
    nome="Salamandra Infernal",
    hp=120,
    ataque=20,
    imagem_path="imagens/salamandra.png"
)

sereia_mistica = CriaturaAgua(
    nome="Sereia Mística",
    hp=130,
    ataque=18,
    imagem_path="imagens/sereia.png"
)

kraken_profundo = CriaturaAgua(
    nome="Kraken Profundo",
    hp=200,
    ataque=30,
    imagem_path="imagens/kraken.png"
)
# Tópico Python: Listas
# A lista 'bestiario' é uma coleção que armazena nossos objetos.
# Ela nos permite gerenciar e acessar todas as criaturas de forma organizada.
bestiario = [
    dragao_chama,
    salamandra_infernal,
    sereia_mistica,
    kraken_profundo
]

