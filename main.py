# Tópico Python: Importando Módulos
# Importamos a biblioteca para a interface gráfica e nosso 
# banco de dados de criaturas.
import PySimpleGUI as sg
from banco_de_dados import bestiario # A lista de objetos que 
#criamos no Dia 1

# Tópico POO: Abstração
# A classe PokedexApp vai 'abstrair' toda a complexidade da 
# interface.
# O código principal só precisará criar um objeto desta 
# classe e chamar um método.
class PokedexApp:
    """
    Classe principal que gerencia toda a lógica da interface 
    gráfica (GUI).
    """

    # Tópico POO: __init__ e self
    # O construtor configura o estado inicial da nossa aplicação.
    def __init__(self):
        # Tópico POO: Encapsulamento
        # A lista de criaturas e o índice atual são atributos 
        # encapsulados,
        # gerenciados internamente pela nossa aplicação.
        self.bestiario = bestiario
        self.indice_atual = 0

        # Define o tema da janela para um visual mais agradável
        sg.theme("DarkBlue3")

        # Tópico PySimpleGUI: Layout em Lista de Listas
        # Cada lista interna representa uma linha na nossa janela.
        # As 'keys' (ex: '-NOME-') são identificadores únicos para cada elemento.
        layout = [
            [sg.Text("MEU BESTIÁRIO DIGITAL", font=("Helvetica", 20), justification="center", expand_x=True)],
            [sg.Image(key='-IMAGEM-', size=(200, 200), background_color='lightgray')],
            [sg.Text("Nome:", font=("Helvetica", 12)), sg.Text("", key='-NOME-', font=("Helvetica", 14, "bold"))],
            [sg.Text("Tipo:", font=("Helvetica", 12)), sg.Text("", key='-TIPO-', font=("Helvetica", 12))],
            [sg.Text("HP:", font=("Helvetica", 12)), sg.Text("", key='-HP-', font=("Helvetica", 12))],
            [sg.Text("Ataque:", font=("Helvetica", 12)), sg.Text("", key='-ATAQUE-', font=("Helvetica", 12))],
            [sg.Multiline("", key='-DESCRICAO-', font=("Helvetica", 11), size=(40, 4), disabled=True, no_scrollbar=True)],
            [sg.Button("Anterior"), sg.Button("Próximo")]
        ]

        # Cria a janela usando o layout definido
        self.window = sg.Window("Bestiário Digital", layout, element_justification='center')

    def atualizar_tela(self, criatura):
        """
        Recebe um objeto Criatura e atualiza todos os elementos da tela.
        """
        # Tópico PySimpleGUI: Atualizando Elementos
        # Usamos a 'key' de cada elemento para acessá-lo e chamar o método .update()
        self.window['-NOME-'].update(criatura.nome)
        self.window['-TIPO-'].update(f"Tipo: {criatura.tipo}")
        self.window['-HP-'].update(f"HP: {criatura.hp}")
        self.window['-ATAQUE-'].update(f"Ataque: {criatura.ataque}")
        
        # Tópico POO: Polimorfismo em Ação!
        # Chamamos o método .descrever() sem nos preocuparmos se a criatura
        # é de Fogo ou Água. O objeto correto sabe como se descrever.
        self.window['-DESCRICAO-'].update(criatura.descrever())
        
        # Atualiza a imagem (será implementado na Aula 2D)
        self.window['-IMAGEM-'].update(filename=criatura.imagem_path)


    def iniciar(self):
        """
        Inicia a aplicação, contendo o loop principal de eventos.
        """
        # Carrega a primeira criatura na tela assim que o programa inicia
        self.atualizar_tela(self.bestiario[self.indice_atual])

        # Tópico PySimpleGUI: Loop de Eventos
        # O programa fica "preso" neste loop, esperando por ações do usuário.
        while True:
            # window.read() espera por um evento (ex: clique de botão)
            event, values = self.window.read()

            # Lógica para fechar o programa
            if event == sg.WIN_CLOSED:
                break
            
            # (A lógica de navegação será adicionada na Aula 2C)

        # Fecha a janela de forma limpa ao sair do loop
        self.window.close()


# --- Ponto de Entrada do Programa ---
# Tópico Python: Bloco 'if __name__ == "__main__"'
# Garante que o código abaixo só será executado quando este arquivo for
# o script principal, e não quando for importado por outro.
if __name__ == "__main__":
    # Tópico POO: Instanciação
    # Criamos o objeto principal da nossa aplicação.
    app = PokedexApp()
    # E chamamos seu método principal para iniciar. Toda a complexidade está
    # escondida (abstraída) dentro do objeto 'app'.
    app.iniciar()
