from kivy.app import App
from calculator import Calculator



class MainApp(App):

    
    def build(self):
        return Calculator()

MainApp().run()