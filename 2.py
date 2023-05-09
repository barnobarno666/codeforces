import kivy
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        self.window=Gridlayout()
        return Label(text='Hello, Kivy!')

TestApp().run()e