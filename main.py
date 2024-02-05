from kivy.app import App
from kivy.core.window import Window
from calculator import Calculator



class MainApp(App):

    
    def build(self):
        return Calculator()

MainApp().run()