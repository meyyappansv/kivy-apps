#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # initialize infinite keyword
    def __init__(self,**kwargs):
        ## Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        ## Set columns 
        self.cols = 2

         ## Add widgets 
        #Add Label
        self.add_widget(Label(text="Name: "))
        ## Add Input Box 
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)


        self.add_widget(Label(text="Favorite Pizza:"))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color:"))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

       
        self.submit = Button(text="Submit",font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f'Hello your name is {name}, your favorite pizza is {pizza}, your favorite color is {color}')
        self.add_widget(Label(text=f'Hello your name is {name}, your favorite pizza is {pizza}, your favorite color is {color}'))
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
