# Importando a lista de objetos do nosso módulo de banco de dados
from banco_de_dados import bestiario

# --- SCRIPT PRINCIPAL DE TESTE ---

print("="*40)
print("   BEM-VINDO AO BESTIÁRIO DIGITAL (v0.1)")
print("="*40)
print("\nListando todas as criaturas do nosso banco de dados:\n")

# Tópico Python: Iteração (Loop for)
# Estamos usando um loop 'for' para passar por cada objeto 'criatura'
# que está armazenado na lista 'bestiario'.

for criatura in bestiario:
    
    # Aqui, a MÁGICA do POLIMORFISMO acontece!
    # Não precisamos saber se a 'criatura' é do tipo Fogo ou Água.
    # Apenas chamamos o método .descrever(), e o Python executa
    # a versão correta do método para aquele objeto específico.
    print(criatura.descrever())
    print("-" * 20)