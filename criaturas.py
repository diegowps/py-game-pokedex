# Tópico Python: Módulos
# Estamos criando nosso primeiro módulo, que conterá as definições (classes)
# das nossas criaturas. Este arquivo poderá ser importado por outros.

# --- CLASSE PAI (Superclasse) ---

# Tópico POO: Classes e Objetos
# A 'class' é o molde, a planta para criar objetos.
class Criatura:
    """
    Representa a criatura base do nosso bestiário.
    Define os atributos e métodos que são comuns a todos os seres.
    """
    # Tópico POO: __init__ e self
    # O método __init__ é o "construtor", chamado automaticamente ao criar um objeto.
    # 'self' se refere à instância específica do objeto que está sendo criada.
    def __init__(self, nome: str, tipo: str, hp: int, ataque: int, imagem_path: str):
        # Tópico POO: Encapsulamento
        # Os atributos (dados) são agrupados e "encapsulados" dentro do objeto.
        # Eles definem o estado de cada criatura.
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.imagem_path = imagem_path

    def descrever(self):
        """
        Método que retorna uma descrição básica da criatura.
        Este é o método que demonstra o Polimorfismo quando sobrescrito.
        """
        # Tópico Python: f-strings
        # Usamos f-strings para formatar o texto de forma limpa e legível.
        return f"Nome: {self.nome} | Tipo: {self.tipo} | HP: {self.hp} | Ataque: {self.ataque}"


# --- CLASSES FILHAS (Subclasses) ---

# Tópico POO: Herança
# A classe 'CriaturaFogo' herda da classe 'Criatura', indicada pelos parênteses.
# Ela ganha todos os atributos e métodos da classe pai automaticamente.
class CriaturaFogo(Criatura):
    """ Uma criatura especializada do tipo Fogo. """
    def __init__(self, nome: str, hp: int, ataque: int, imagem_path: str):
        # Tópico POO: super()
        # A função super() chama o método da classe pai.
        # Aqui, estamos reutilizando o __init__ de 'Criatura' para não repetir código.
        super().__init__(nome, "Fogo", hp, ataque, imagem_path)
 # Tópico POO: Polimorfismo (Sobrescrita de Método)
    # Este método 'descrever' tem o mesmo nome do método na classe pai,
    # mas se comporta de forma diferente (polimorfismo).
    def descrever(self):
        # Reutilizamos a descrição base da classe pai
        descricao_base = super().descrever()
        # E adicionamos um comportamento específico para criaturas de fogo
        return descricao_base + " | Habilidade: Seu corpo queima em chamas!"

class CriaturaAgua(Criatura):
    """ Uma criatura especializada do tipo Água. """
    def __init__(self, nome: str, hp: int, ataque: int, imagem_path: str):
        # Reutilizando o construtor da classe pai
        super().__init__(nome, "Água", hp, ataque, imagem_path)

    # Polimorfismo novamente: outra forma para o mesmo método
    def descrever(self):
        descricao_base = super().descrever()
        return descricao_base + " | Habilidade: Vive nas profundezas do oceano."
