import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import webbrowser
class Topico:
    def _init_(self, titulo):
        self.titulo = titulo

class GerenciadorDeTopicos(App):
    def build(self):
        self.topicos = []
        self.carregar_topicos()
        layout = BoxLayout(orientation='vertical')
        self.scroll_view = ScrollView()
        layout_interno = BoxLayout(orientation='vertical', size_hint_y=None)
        layout_interno.height = 0
        self.lista_topicos = BoxLayout(orientation='vertical', size_hint_y=None)
        self.lista_topicos.height = 0
        layout_interno.add_widget(self.lista_topicos)
        self.entry_titulo = TextInput(hint_text='Digite o título do tópico', size_hint_y=None, height=100)
        layout_interno.add_widget(self.entry_titulo)
        botao_adicionar = Button(text='Adicionar', size_hint_y=None, height=100)
        botao_adicionar.bind(on_press=self.adicionar_topico)
        layout_interno.add_widget(botao_adicionar)
        self.scroll_view.add_widget(layout_interno)
        layout.add_widget(self.scroll_view)
        self.atualizar_lista_topicos()
        return layout

    def carregar_topicos(self):
        if os.path.exists("topicos.txt"):
            with open("topicos.txt", "r") as arquivo:
                for linha in arquivo:
                    self.topicos.append(Topico(linha.strip()))

    def salvar_topicos(self):
        with open("topicos.txt", "w") as arquivo:
            for topico in self.topicos:
                arquivo.write(topico.titulo + "\n")

    def adicionar_topico(self, instance):
        titulo = self.entry_titulo.text
        if titulo:
            topico = Topico(titulo)
            self.topicos.append(topico)
            self.salvar_topicos()
            self.atualizar_lista_topicos()
            self.entry_titulo.text = ''

    def atualizar_lista_topicos(self):
        self.lista_topicos.clear_widgets()
        self.lista_topicos.height = 0
        for i, topico in enumerate(self.topicos):
            layout_topico = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)

            label_topico = Label(text=f"{i+1}. {topico.titulo}")
            layout_topico.add_widget(label_topico)

            botao_pesquisar = Button(text='Pesquisar', size_hint_x=None, width=180)
            botao_pesquisar.bind(on_press=lambda instance, topico=topico: self.pesquisar(topico))
            layout_topico.add_widget(botao_pesquisar)

            botao_excluir = Button(text='Deletar', size_hint_x=None, width=180)
            botao_excluir.bind(on_press=lambda instance, topico=topico: self.excluir(topico))
            layout_topico.add_widget(botao_excluir)

            self.lista_topicos.add_widget(layout_topico)
            self.lista_topicos.height += layout_topico.height
            self.lista_topicos.parent.height = self.lista_topicos.height + 200  # Ajuste a altura do layout_interno

    def pesquisar(self, topico):
        webbrowser.open(f"https://www.google.com/search?q={topico.titulo}")

    def excluir(self, topico):
        self.topicos.remove(topico)
        self.salvar_topicos()
        self.atualizar_lista_topicos()

if __name__ == "__main__":
    GerenciadorDeTopicos().run()