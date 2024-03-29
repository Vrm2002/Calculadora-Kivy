from kivy.uix.screenmanager import Screen
import math

class Calculator(Screen):

    def calculate(self,*args):
        calc_entry = self.ids.txtinput.text
        if calc_entry !='':
            try:
                if calc_entry[0] in '1234567890()-+':
                    self.ids.txtinput.text = str(eval(calc_entry))
            except:
                self.ids.txtinput.text = 'Error'

    def ac_clear(self):
        self.ids.txtinput.text = ''

    def delete(self):
        self.ids.txtinput.text = self.ids.txtinput.text[:-1]

    def percentage(self):
        try:
            per = self.ids.txtinput.text+'*100'
            self.ids.txtinput.text = str(eval(per))
        except:
            self.ids.txtinput.text = 'Error'

    
            
    def rad(self):
       try:
           value = self.ids.txtinput.text
           new_value = math.radians(int(value))
           self.ids.txtinput.text = str(new_value)
       except:
          self.ids.txtinput.text = 'Error' 

       
    def dot(self):

        value = self.ids.txtinput.text
        try:
            if value == '':
                self.ids.txtinput.text = '0.'
            elif value[-1] == '.':
                pass
            else:
                self.ids.txtinput.text = value + "."
        except:
          self.ids.txtinput.text = 'Error'

    def pi(self):
        self.ids.txtinput.text = self.ids.txtinput.text + str((math.pi))

    def raiz(self):
        try:
           value = self.ids.txtinput.text
           new_value = math.sqrt(float(value))
           self.ids.txtinput.text = str(new_value)
        except:
          self.ids.txtinput.text = 'Error' 



    