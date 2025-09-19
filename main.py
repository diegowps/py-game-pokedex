import PySimpleGUI as sg
from banco_de_dados import bestiario

class PokedexApp:
    def __init__(self):
        self.bestiario = bestiario
        self.indice_atual = 0

        sg.theme("DarkBlue3")

        coluna_info = [
            [sg.Text("Nome:", font=("Helvetica", 12)), sg.Text("", key='-NOME-', font=("Helvetica", 14, "bold"))],
            [sg.Text("Tipo:", font=("Helvetica", 12)), sg.Text("", key='-TIPO-', font=("Helvetica", 12))],
            [sg.Text("HP:", font=("Helvetica", 12)), sg.Text("", key='-HP-', font=("Helvetica", 12))],
            [sg.Text("Ataque:", font=("Helvetica", 12)), sg.Text("", key='-ATAQUE-', font=("Helvetica", 12))],
            [sg.Multiline("", key='-DESCRICAO-', font=("Helvetica", 11), size=(40, 4), disabled=True, no_scrollbar=True)]
        ]

        layout = [
            [sg.Text("MEU BESTIÁRIO DIGITAL", font=("Helvetica", 20), justification="center", expand_x=True)],
            [sg.Image(key='-IMAGEM-', size=(200, 200), background_color='lightgray')],
            [sg.Column(coluna_info, element_justification='left')],
            [sg.Button("Anterior"), sg.Button("Próximo")]
        ]

        # A CORREÇÃO ESTÁ AQUI! Adicionamos o parâmetro finalize=True.
        self.window = sg.Window("Bestiário Digital", layout, element_justification='center', finalize=True)

    def atualizar_tela(self, criatura):
        """ Recebe um objeto Criatura e atualiza todos os elementos da tela. """
        self.window['-NOME-'].update(criatura.nome)
        self.window['-TIPO-'].update(criatura.tipo)
        self.window['-HP-'].update(criatura.hp)
        self.window['-ATAQUE-'].update(criatura.ataque)
        self.window['-DESCRICAO-'].update(criatura.descrever())
        self.window['-IMAGEM-'].update(filename=criatura.imagem_path)

    def iniciar(self):
        """ Inicia a aplicação, contendo o loop principal de eventos. """
        # Com finalize=True, esta chamada agora funciona perfeitamente.
        self.atualizar_tela(self.bestiario[self.indice_atual])

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == "Anterior":
                if self.indice_atual > 0:
                    self.indice_atual -= 1
                    self.atualizar_tela(self.bestiario[self.indice_atual])

            elif event == "Próximo":
                if self.indice_atual < len(self.bestiario) - 1:
                    self.indice_atual += 1
                    self.atualizar_tela(self.bestiario[self.indice_atual])

        self.window.close()

if __name__ == "__main__":
    app = PokedexApp()
    app.iniciar()