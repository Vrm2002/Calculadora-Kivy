from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class CalculatorApp(App):
    def build(self):
        self.expression = TextInput(font_size=32, multiline=False, readonly=True, halign='right', background_color=(1,1,1,0.8))
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.expression)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['sqrt', '(', ')', '^2'],
            ['Ce']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, on_press=self.on_button_press, background_color=(0.7, 0.7, 0.7, 1))
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current_text = self.expression.text

        if instance.text == '=':
            try:
                result = str(eval(current_text))
                self.expression.text = result
            except Exception as e:
                self.expression.text = "Error"
        elif instance.text == 'sqrt':
            try:
                result = str(math.sqrt(float(current_text)))
                self.expression.text = result
            except ValueError:
                self.expression.text = "Error"
        elif instance.text == 'Ce':
            self.expression.text = current_text[:-1]
        else:
            self.expression.text = current_text + instance.text

if __name__ == '__main__':
    CalculatorApp().run()
