#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
   
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'Hello your name is {name}, your favorite pizza is {pizza}, your favorite color is {color}')
        #self.add_widget(Label(text=f'Hello your name is {name}, your favorite pizza is {pizza}, your favorite color is {color}'))
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
